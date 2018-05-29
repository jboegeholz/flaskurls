import tempfile
import unittest

import os

from test.testapp_permissions.application import create_app


class FlaskUrlsTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.db_fd, self.app.config['DATABASE'] = tempfile.mkstemp()
        self.test_app = self.app.test_client()
        self.test_app.testing = True

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.app.config['DATABASE'])

    def login(self, context, username, password):
        return context.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def test_require_roles(self):
        from flask_url_mapping import FlaskUrls
        from test.testapp_permissions import views
        self.app.config.update(dict(
            SECRET_KEY='development key',
            USERNAME='admin',
            PASSWORD='default',
            ROLES='admin'
        ))
        urls = [
            ("/index", views.index, ["GET"]),
            ("/login", views.login, ["GET", "POST"]),
            ("/admin", views.admin, ["GET"], "admin"),
        ]
        flask_urls = FlaskUrls(self.test_app.application)
        flask_urls.register_urls(urls)
        with self.app.test_client() as c:
            rv = self.login(c, 'admin', 'default')
            result = c.get('/admin')
        self.assertEqual(result.status_code, 200)

    def test_require_roles_no_access(self):
        from flask_url_mapping import FlaskUrls
        from test.testapp_permissions import views
        self.app.config.update(dict(
            SECRET_KEY='development key',
            USERNAME='user',
            PASSWORD='default',
            ROLES='user'
        ))
        urls = [
            ("/index", views.index, ["GET"]),
            ("/login", views.login, ["GET", "POST"]),
            ("/admin", views.admin, ["GET"], "admin"),
        ]
        flask_urls = FlaskUrls(self.test_app.application)
        flask_urls.register_urls(urls)
        with self.app.test_client() as c:
            rv = self.login(c, 'user', 'default')
            result = c.get('/admin')
        self.assertEqual(result.status_code, 404)