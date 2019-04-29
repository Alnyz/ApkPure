# ApkPure Unofficial Wrapper ✨
_Search, Simplify detail & Downloadable from Apkpure.com_

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a9cbc42bde0c4baa9122c2010485d0b0)](https://app.codacy.com/app/dyseo/ApkPure?utm_source=github.com&utm_medium=referral&utm_content=dyseo/ApkPure&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/dyseo/ApkPure.svg?branch=master)](https://travis-ci.org/dyseo/ApkPure) [![Python](https://img.shields.io/badge/Python-3.6%20%7C%203.7-brightgreen.svg)](pytho.org) [![License](https://img.shields.io/badge/MIT-License-blue.svg)](https://opensource.org/licenses/MIT)
___
## Features
1. Simply to use
2. Readable
3. Using async request & multithreading for really fast request (not really sure)
4. Easy accessing dictionary

## Installing
- `git clone https://github.com/dyseo/ApkPure`
- `cd ApkPure`
- `pip3 install -r requirements.txt`


## How to
```python
from apis import ApkPure

apk = ApkPure(return_as="dict")
#set 'dict' or 'rpc' for returning as
```

### Search Application
```python
search = api._search("pubg")
print(search)
```

### Get Details from giving url
```python
details = api.detail_from_url(search.results[0].url)
print(details)

# or you can do simple like this

detail = api.this_detail(search, 1)
print(detail)
```

### Download application
```python
api.download_(url=detail.url_download, name=detail.title, ex=detail.extension, path="/downloads)
```

# Author
Dyseo / [Dyseo](https://github.com/dyseo)
