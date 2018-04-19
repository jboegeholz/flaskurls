from flask import render_template


def home_index():
    return "hello home index!"


def home_users():
    return "hello home users!"


def home_html():
    return render_template("index.html")
