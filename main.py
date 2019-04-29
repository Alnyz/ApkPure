from apis.api import ApkPure

api = ApkPure(return_as="rpc")
find = api._search("config pubg")
this = api.this_detail(find, 1)
print(this)
