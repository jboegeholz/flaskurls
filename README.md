# flask_url_mapping
Django-style url handling for Flask

Inspired by [https://stackoverflow.com/questions/31680048/django-styled-flask-url-pattern-for-large-application]
this package is an attempt to generalize the concept of Django-like url-view / endpoint-mapping.

You can install it via 
```
pip install flask-url-mapping
```

Centerpiece is an urls.py which contains the mapping.
```
urls = [
    ("/", views.index, ["GET"]),
    ("/users", views.get_users, ["GET"]),
    ("/home", "home.urls")
]
```
You can either directly map urls to views/endpoints or include another urls file from a component. 
In the ladder case the "url" is the prefix for all urls in the sub-component.

The syntax is `(<route>, <function>, <http_method>)` or `(<prefix>, <module>)`

After declaring your url mapping You can register the urls to the flask app via `register_urls`
       

A sample setup 
* wsgi.py
```
from flask import Flask
from flask_url_mapping import register_urls
from urls import urls
app = Flask(__name__)


if __name__ == '__main__':
    register_urls(app, urls)
    app.run()
```
* urls.py
```
from views import *
urls = [
    ("/", hello_world, ["GET"])
]
```
* views.py
```
def hello_world():
    return 'Hello World!'    
```

## Components
A component is a subfolder which contains at least an urls.py and an views.py

When this folder also contains a templates directory, it will be automatically added to the jinja2 search path for html templates

## Travis-CI
[![Build Status](https://travis-ci.org/jboegeholz/flaskurls.svg?branch=master)](https://travis-ci.org/jboegeholz/flaskurls)