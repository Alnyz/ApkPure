from .etc import Search, DetailApk, TrandingApk
from .download_apk import DownloadApk
from style.body import ResponseDetail, PreObject, ResponseObject, SimpleDict
from typing import Union

class ApkPure(object):
	def __init__(self, return_as="dict"):
		self.return_as = return_as

	def _search(self, query: str) -> Union[dict, ResponseObject]:
		"""
		Search application android using query

		:param query: string what you want to search it
		:returnType: dict if return_as set as dict otherwise classes from Response-RPC 
		"""
		assert self.return_as in ["dict", "rpc"], "'return_as' should be 'rpc' or 'dict' not <%s>" % self.return_as
		s = Search(query)
		data = s.search_apk()
		if self.return_as == "dict":
			read = SimpleDict(data).read
		if self.return_as == "rpc":
			read = ResponseObject()
			read.read(data)
		return read
		
	def detail_from_url(self, url: str) -> Union[dict, ResponseDetail]:
		"""
		Use this method to get detail and download url from specifict URL
		pass as full url from apkpure.com site or get it using '_search' method
		
		:param url: string url to parse it
		:returnType: dict if return_as set as dict otherwise classes from Response-RPC
		"""
		assert self.return_as in ["dict", "rpc"], "'return_as' should be 'rpc' or 'dict' not <%s>" % self.return_as
		s = DetailApk(url)
		data = s.detail_apk()
		if self.return_as == "dict":
			read = SimpleDict(data).read
		if self.return_as == "rpc":
			read = ResponseDetail()
			read.read(data)
		return read
	
	def _tranding(self) -> Union[dict, ResponseObject]:
		"""
		Use this method to know 24h tranding application fromapk.pure
		
		:returnType: dict if return_as set as dict otherwise classes from Response-RPC
		"""
		assert self.return_as in ["dict", "rpc"], "'return_as' should be 'rpc' or 'dict' not <%s>" % self.return_as
		s = TrandingApk()
		data = s.list_tranding()
		if self.return_as == "dict":
			read = SimpleDict(data).read
		if self.return_as == "rpc":
			read = ResponseDetail()
			read.read(data)
		return read
	
	def this_detail(self, data: dict,  numc: int) -> Union[dict, ResponseObject]:
		"""
		use this method to get detial from specifict data
		
		:param data: dict or <class ResponseObject> to parse it
		:param numc: number of index which you want to return it
		
		:returnType: dict if return_as set as dict otherwise classes from Response-RPC
		"""
		assert self.return_as in ["dict", "rpc"], "'return_as' should be 'rpc' or 'dict' not <%s>" % self.return_as
		x = data.results[int(numc)-1]
		ret = self.detail_from_url(x.url)
		if self.return_as == "dict":
			read = SimpleDict(ret).read
		if self.return_as == "rpc":
			read = ResponseDetail()
			read.read(ret)
		return read
	
	def download_(self, url, name, ex):
		x = DownloadApk(name=name, extension=ex)
		x.download_apk(url)