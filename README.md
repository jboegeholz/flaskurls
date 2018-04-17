# flask_urls
Django-style url handling for Flask

Inspired by [https://stackoverflow.com/questions/31680048/django-styled-flask-url-pattern-for-large-application]
this package is an attempt to generalize the concept of Django-like url-view / endpoint-mapping.

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

#Travis-CI
[![Build Status](https://travis-ci.org/jboegeholz/flaskurls.svg?branch=master)](https://travis-ci.org/jboegeholz/flaskurls)