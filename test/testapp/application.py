from __future__ import print_function

from flask import Flask
from flask_urls import register_urls
from test.testapp.urls import urls

__all__ = ['create_app']


def create_app():
    app = Flask(__name__)
    register_urls(app, urls)
    return app




