# -*- coding: utf-8 -*-
import grequests as reqs

from .config import config
from threading import Thread

from queue import Queue
import logging, threading

log = logging.getLogger(__name__)

class Connect(config):
	def __init__(self,
						headers=None,
						timeout=30,
						proxy=None):
		super(Connect, self).__init__()
		self.headers = headers if headers is not None else self.default_header
		self.proxy = proxy
		self.timeout = timeout
		self.base_url = "https://apkpure.com"
		self.concurrent = 200
		self.queue = Queue(self.concurrent * 2)
		self.event = threading.Event()
		self.data = None

	def request(self, url, callback = lambda x, y: print(x, y)):
		url = [url]
		req = (reqs.get(u, timeout=self.timeout,
									headers=self.headers,
									proxies=self.proxy)
									for u in url)
		s = reqs.map(req, exception_handler=callback)
		for i in s:
			if i.ok:
				return i

	def do_work(self):
		url = self.queue.get()
		ret = self.request(url)
		self.data = ret
		self.queue.task_done()
		self.stop_th()

	def result(self):
		return self.data
		
	def stop_th(self):
		self.event.set()
		
	def startwork(self, urls):
		for i in range(self.concurrent):
			t = Thread(target=self.do_work)
			t.daemon = True
			t.start()
		
		self.queue.put(urls)
		self.queue.join()