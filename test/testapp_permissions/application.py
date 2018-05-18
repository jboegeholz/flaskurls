from __future__ import print_function

from flask_login import LoginManager

from test.testapp_permissions.user import User

login_manager = LoginManager()

from flask import Flask

__all__ = ['create_app']


@login_manager.user_loader
def load_user(user_id):
    return User()

def create_app():
    app = Flask(__name__)
    login_manager.init_app(app)
    return app




