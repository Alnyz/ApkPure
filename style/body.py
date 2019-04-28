from .response import ResponseJson, ResponseRpc

class PreObject(ResponseRpc):
	def __init__(self, title=None, url=None, img_url=None):
		super(PreObject, self).__init__()
		self.title =  title
		self.url = url
		self.img_url = img_url
		
	def read(self, obj):
		self.title = obj.get("title", None)
		self.url = obj.get("url", None)
		self.img_url = obj.get("img_url", None)
	
class ResponseObject(ResponseRpc):
	def __init__(self, results=None):
		super(ResponseObject, self).__init__()
		self.results = results
		
	def read(self, obj):
		for k in obj.get("results", []):
			if self.results is None:
				self.results = []
			r = PreObject()
			r.read(k)
			self.results.append(r)

class ResponseDetail(ResponseRpc):
	def __init__(self,
					title = None,
					icon = None,
					url_download = None,
					desc = None,
					extension = None
				):
		super(ResponseDetail, self).__init__()
		self.title = None
		self.icon = None
		self.url_download = None
		self.desc = None
		self.extension = None
		
	def read(self, obj):
		self.title = obj.get("title", None)
		self.extension = obj.get("extension", None)
		self.icon = obj.get("icon", None)
		self.url_download = obj.get("url_download", None)
		self.desc = obj.get("desc", None)
		
		
class SimpleDict(object):
	def __init__(self, data):		
		self.read = ResponseJson(data)