from .webdav import WebDavClient
from .credential import *

client = WebDavClient(
    'nutstore',
    username=NUTSTORE_USERNAME,
    password=NUTSTORE_PASSWORD,
    working_dir='/',
    check_conn=False
)