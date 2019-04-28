from .etc import Downloads
from connecting import Connect

import os
class DownloadApk(Downloads):
	def __init__(self, name, extension, path=None):
		super(DownloadApk, self).__init__()
		self.name = self.rename(name.lower())
		self.extension = ".{}".format(extension)
		self.path = path if path is not None else os.path.realpath("")+"/"
		
	
	def rename(self, name):
		return name.replace(" ", "_")
	
	def save_(self, content):
		with open(self.path+self.name+self.extension, "wb") as fp:
			fp.write(content)
		print("\033[1;37;40mDownload Succesfully, file store at",fp.name, end="")

	def download_apk(self, url):
		print("\033[1;37;40mDownload started..")
		get = self.request(url)
		self.save_(get.content)