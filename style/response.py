# -*- coding: utf-8 -*-
class ResponseRpc(object):
	def __init__(self):
		super(ResponseRpc, self).__init__()

	def read(self):
		pass

	def write(self):
		pass

	def __getitem__(self, key):
		return getattr(self, key, None)

	def __setitem__(self, key, val):
		return setattr(self, key, val)

	def keys(self):
		return self.__dict__.keys()

	def values(self):
		return self.__dict__.values()

	def items(self):
		return self.__dict__.items()

	def __eq__(self, obj):
		return self.__class__.__name__ == obj.__class__.__name__

	def __repr__(self):
		L=['%s=%r'%(key, value) for key, value in self.items()]
		return '<%s(%s)>'%(self.__class__.__name__, ', '.join(L))
	
class ResponseJson(dict):
	__setattr__= dict.__setitem__  
	__delattr__= dict.__delitem__
	
	def __init__(self, xdata):
		data = xdata		
		for name, value in data.items():
			setattr(self, name, self._wrap(value))

	def __getattr__(self, attr):
		return self.get(attr, None)
		
	def _wrap(self, value):  # Reff http://stackoverflow.com/questions/1305532/convert-python-dict-to-object
		if isinstance(value, (tuple, list, set, frozenset)):
			return type(value)([self._wrap(v) for v in value])
		else:
			if isinstance(value, dict):
				return ResponseJson(value)
			else:
				return value