# -*- coding: utf-8 -*-
from connecting import Connect
from bs4 import BeautifulSoup as Soup
from bs4.element import Tag

import re

class Downloads(Connect):
	def __init__(self):
		super(Downloads, self).__init__()
		self.URL_RE = r"=(\w+)$"
	
	def sub_url(self, url):
		return re.sub(self.URL_RE, "=details", url)
		
	def get_dw_url(self, u):
		"""
		TODO: make this URL consistence with endswith 'details' for easly parsing
		"""
		if not u.endswith("details"):
			u = sub_url(u)
		self.startwork(u)
		response = self.result()
		soup = Soup(response.text, "lxml")
		page = soup.find("div", class_="main page-q")
		find_url = page.find("div", class_ = "fast-download-box")
		url = find_url.find("a", attrs={"id":"download_link"})				
		return url["href"], url["title"].split(" ")[-1]
		
class Search(Connect):
	def __init__(self, query: str = None):
		super(Search, self).__init__()
		assert query is not None, "Please fill this query first"
		self.query = query
		
	def search_apk(self) -> Tag:
		self.startwork(self.base_url+self.search.format(self.query))
		response = self.result()
		soup = Soup(response.text, "lxml")
		ret = soup.find("div", attrs={"id":"search-res"})
		return self.extract_data(ret)
	
	def extract_data(self, data: Tag) -> dict:
		ret_ = {"results":[]}
		for i in data.find_all("dl", class_="search-dl"):
			dl = i.find("dt")
			url, title = dl.find("a")["href"], dl.find("a")["title"]
			img = dl.find("img")["src"]
			ret_["results"].append({
				"title":title.title(),
				"url":url,
				"img_url":img
			})
		return ret_

class DetailApk(Downloads):
	def __init__(self, ended_url: str = None):
		super(DetailApk, self).__init__()
		if self.base_url in ended_url:
			self.ended_url = ended_url
		else:			
			self.ended_url = self.base_url+ended_url

		self.xdata = dict(
						title = None,
						icon = None,
						extension = None,
						url_download = None,
						desc = None
					)

	def detail_apk(self) -> dict:
		self.startwork(self.ended_url)
		response = self.result()
		soup = Soup(response.text, "lxml")
		box = soup.find("div", class_ = "box")
		title = box.find("div", class_="title-like").text
		icon = box.find("div", class_="icon").find("img")["src"]
		desc = box.find("div", class_="description").find("div", class_="content").text
		url_dw = self.base_url+box.find("div", class_="ny-down").find("a", class_="da")["href"]
		dwl = self.get_dw_url(url_dw)		
		self.xdata["title"] = title.strip()
		self.xdata["url_download"] = dwl[0]
		self.xdata["extension"] = dwl[1]
		self.xdata["icon"] = icon
		self.xdata["desc"] = self.parse_lenght(desc)
		return self.xdata

class TrandingApk(Downloads):
	def __init__(self):
		super(TrandingApk, self).__init__()
		self.xdata = dict(results=list())
	
	def list_tranding(self):
		self.startwork(self.base_url+self.tranding)
		response = self.result()
		soup = Soup(response.text, "lxml")
		find = soup.find("div", class_="left floatr")
		for i in find.select("ul > li"):
			temp, down = i.find("div", class_="category-template-img"), i.find("div", class_="category-template-down")
			img = temp.find("img")["data-original"]
			title = temp.find("a")["title"]
			dwl = self.base_url+down.find("a")["href"]
			self.xdata["results"].append({
				"title":title,
				"img_url":img,
				"download_link":self.sub_url(dwl)
			})
		return self.xdata
