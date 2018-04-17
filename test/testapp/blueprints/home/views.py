from flask import Blueprint

home_bp = Blueprint('home', __name__, template_folder='templates')


def index():
    return "hello home index!"


def get_users():
    return "hello home users!"

