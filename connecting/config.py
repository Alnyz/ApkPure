class config:
	def __init__(self):	
		self.search = "/search?q={}"
		self.tranding = "/game-24h"
		self.discover = "/discover"
		self.default_header = {"User-Agent":"Python/requests"}
	
	def parse_lenght(self, string: str) -> str:
		min = 100
		if len(string) > 300 or len(string) < 250:
			lenght = len(string) / 2 - min if len(string) > 300 else 70
			return string.replace(string[-int(lenght)::], "...")