from flask import Flask

app = Flask(__name__)


# https://stackoverflow.com/questions/31680048/django-styled-flask-url-pattern-for-large-application

if __name__ == '__main__':
    from app import create_app
    web_app = create_app()
    from gevent.wsgi import WSGIServer
    http_server = WSGIServer(('0.0.0.0', 8000), web_app)
    http_server.serve_forever()


