import unittest
from test.testapp_permissions.application import create_app


class FlaskUrlsTest(unittest.TestCase):
    def setUp(self):
        # creates testapp under test
        self.test_app = create_app().test_client()
        self.test_app.testing = True

    def tearDown(self):
        pass

    def test_require_roles(self):
        from flask_url_mapping import FlaskUrls
        from test.testapp import views
        urls = [
            ("/admin", views.admin, ["GET"], "admin"),
        ]
        flask_urls = FlaskUrls(self.test_app.application)
        flask_urls.register_urls(urls)
        result = self.test_app.get('/admin')
        self.assertEqual(result.status_code, 200)