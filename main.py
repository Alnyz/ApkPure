from apis.api import ApkPure

api = ApkPure(return_as="dict")
find = api._search("config pubg")
this = api.this_detail(find, 1)
api.download_(this.url_download, this.title, this.extension)