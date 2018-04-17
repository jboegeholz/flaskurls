from __future__ import print_function
from flask import Flask
from test.testapp.urls import urls


__all__ = ['create_app']


def create_app():
    app = Flask("Blub", template_folder="testapp/templates", static_folder="testapp/static")
    for url in urls:
        app.add_url_rule(url[0], methods=url[1], view_func=url[2])
    return app




