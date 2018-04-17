from __future__ import print_function
from flask import Flask
from urls import urls



__all__ = ['create_app']


def create_app():
    app = Flask("Blub", template_folder="app/templates", static_folder="app/static")
    for url in urls:
        app.add_url_rule(url[0], methods=url[1], view_func=url[2])
    configure_blueprints(app)
    return app


def configure_blueprints(app):
    from app.blueprints.home.views import home_bp
    app.register_blueprint(home_bp)




