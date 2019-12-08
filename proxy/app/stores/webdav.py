import easywebdav
import tempfile

from os.path import basename, splitext
from urllib.parse import urljoin

from .base import BaseClient

class WebDavClient(BaseClient):

    class Context:
        """A helper that wraps pretty remote path to real dav path"""

        def __init__(self, prefix='', start='/'):
            assert start.startswith('/')
            self._prefix = prefix
            self.cwd = start

        def to_full(self, path):
            return '{0}{1}'.format(self._prefix, self._path_resolve(path))

        @property
        def full(self):
            return self.to_full(self.cwd)

        def cd(self, remote_dir):
            self.cwd = self._path_resolve(remote_dir)
            print(self.cwd)

        def _path_resolve(self, path):
            """
            Copied from http-prompt/http_prompt/execution.py
            >>>path_resolve('a', '/b')
            "/b"
            >>>path_resolve('a', 'b')
            "a/b"
            """
            base = self.cwd
            if not base.endswith('/'):
                base = base + '/'
            url = urljoin(base, path)
            if url.endswith('/') and not path.endswith('/'):
                url = url[:-1]
            return url

    apis = {
        'nutstore': {
            'endpoint': 'dav.jianguoyun.com',
            'prefix': '/dav',
        },
    }

    def __init__(self, store, username, password, working_dir, check_conn=True):
        if not working_dir.startswith('/'):
            working_dir = '/' + working_dir
        endpoint = self.apis[store]['endpoint']
        prefix = self.apis[store]['prefix']
        self._context = self.Context(prefix=prefix, start=working_dir)
        self._client = easywebdav.connect(
            endpoint,
            protocol='https',
            username=username,
            password=password
        )
        if check_conn:
            self.check_conn()

    def check_conn(self):
        self.ls()
        return True

    def upload(self, local_path, remote_dir=None):
        name = basename(local_path)
        directory = remote_dir or self.cwd
        remote_path = join(directory, name)
        self._client.upload(local_path, self._full_path(remote_path))

    def download(self, remote_path, local_dir=None):
        local_path = local_path or tempfile.mktemp(suffix=splitext(remote_path)[-1])
        self._client.download(self._full_path(remote_path), local_path)

    def cwd(self):
        return self._context.cwd

    def cd(self, remote_dir):
        self._context.cd(remote_dir)

    def ls(self):
        def file_in_dir(name, path):
            return (path in name) and (name != path)

        full_path = self._context.full
        return filter(lambda f: file_in_dir(f.name, full_path), self._client.ls(full_path))

    def rm(self, remote_path):
        self._client.delete(self._full_path(remote_path))

    def mkdir(self, remote_dir):
        self._client.mkdir(self._full_path(remote_dir))

    def _full_path(self, path):
        """Translate short paths (e.g. /test) to full paths."""
        return self._context.to_full(path)