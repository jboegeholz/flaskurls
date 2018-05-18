from flask import request, session, flash, redirect, url_for, current_app, render_template
from flask_login import login_required, current_user, login_user

from test.testapp_permissions.user import User


def index():
    return "hello index"


def get_users():
    return "hello users!"


@login_required
def admin():
    return "Hello Admin"


def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != current_app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != current_app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            login_user(User())
            return redirect("/index")

