class BaseClient(object):

	@property
	def cwd(self):
		return '/'

	def ls(self):
		return []

	def rm(self, path):
		pass

	def mkdir(self, directory):
		pass

	def upload(self, local_path, remote_dir):
		pass

	def download(self, remote_path, local_dir):
		pass

	def cd(self, remote_dir):
		pass