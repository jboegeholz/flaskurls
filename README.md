# Flask url mapping

Django-style url handling for Flask

Inspired by [this stackoverflow question](https://stackoverflow.com/questions/31680048/django-styled-flask-url-pattern-for-large-application).
this package is an attempt to generalize the concept of Django-like url-view / endpoint-mapping.

## installation

The package is in the [python package index](https://pypi.org/project/flask-url-mapping/).

```sh
pip install flask-url-mapping
```

## Usage

Centerpiece is an urls.py which contains the mapping.

```py
urls = [
    ("/", views.index),                             # 1
    ("/login", views.login, ["GET", "POST"]),       # 2
    ("/home", "home.urls")                          # 3
    ("/admin", views.admin, ["GET"], "admin_role"), # 4
]
```

There are four ways to map routes to endpoints

1. route to endpoint, http method default is GET
2. route to endpoint with array of http methods
3. route to component see Components
4. route to endpoint with array of http methods and required role

After declaring your url mapping You can register the urls to the flask app via `register_urls`

## A sample setup without permissions

* wsgi.py

```py
from flask import Flask
from flask_url_mapping import register_urls
from urls import urls
app = Flask(__name__)

if __name__ == '__main__':
    flask_urls = FlaskUrls(app)
    flask_urls.register_urls(urls)
    app.run()
```

* urls.py

```py
from views import *
urls = [
    ("/", hello_world, ["GET"])
]
```

* views.py

```py
def hello_world():
    return 'Hello World!'    
```

## A sample setup with permissions

When adding a role to a route endpoint mapping your project has to use flask_login

## Components

A component is a subfolder which contains at least an urls.py and an views.py
When this folder also contains a templates directory, it will be automatically added to the jinja2 search path for html templates

## Travis-CI

[![Build Status](https://travis-ci.org/jboegeholz/flaskurls.svg?branch=master)](https://travis-ci.org/jboegeholz/flaskurls)
