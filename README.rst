Url Shortener
=============
[![Build Status](https://travis-ci.org/lil_url.svg?branch=master)](https://travis-ci.org/lil_url)


Current status, version 0.0.1, pre-alpha release
------------------------------------------------

This project is under constant development and maintenance.

Details
-------

Project codebase: <https://github.com/omprakash1989/LilUrl>

Project Documentation: <http://url_shortner.readthedocs.io/en/latest>


Features
--------

- One click installation


Installation
------------

Install lil_url by running:

pip install url_shortener

Contribute
----------

- Issue Tracker: https://github.com/omprakash1989/LilUrl/issues
- Source Code: https://github.com/omprakash1989/LilUrl

License
-------

The project is licensed under the MIT License.

How to use
==========
```python

from flask import Flask
from lil_url import shorten_url, init_app

app = Flask(__name__)
init_app(app)


response = shorten_url("https://google.co.in")
if response.get("success"):
    print("Url Slug: {} \n Absolute Url: {}".format(response.get('slug'), response.get('absolute_url')))

```
