import unittest
from test.testapp.application import create_app


class FlaskUrlsTest(unittest.TestCase):
    def setUp(self):
        # creates testapp under test
        self.test_app = create_app().test_client()
        self.test_app.testing = True

    def tearDown(self):
        pass

    def test_root(self):
        from flask_url_mapping import FlaskUrls
        from test.testapp import views
        urls = [
            ("/", views.index, ["GET"]),
        ]
        flask_urls = FlaskUrls(self.test_app.application)
        flask_urls.register_urls(urls)
        result = self.test_app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_users(self):
        from flask_url_mapping import FlaskUrls
        from test.testapp import views
        urls = [
            ("/users", views.get_users, ["GET"]),
        ]
        flask_urls = FlaskUrls(self.test_app.application)
        flask_urls.register_urls(urls)
        result = self.test_app.get('/users')
        self.assertEqual(result.status_code, 200)

    def test_home_index(self):
        from flask_url_mapping import FlaskUrls
        urls = [
            ("/home", "home.urls")
        ]
        flask_urls = FlaskUrls(self.test_app.application)
        flask_urls.register_urls(urls)
        result = self.test_app.get('/home/home_index')
        self.assertEqual(result.status_code, 200)

    def test_home_users(self):
        from flask_url_mapping import FlaskUrls
        urls = [
            ("/home", "home.urls")
        ]
        flask_urls = FlaskUrls(self.test_app.application)
        flask_urls.register_urls(urls)
        result = self.test_app.get('/home/home_users')
        self.assertEqual(result.status_code, 200)

    def test_without_http_method(self):
        from flask_url_mapping import FlaskUrls
        from test.testapp import views
        urls = [
            ("/", views.index),
        ]
        flask_urls = FlaskUrls(self.test_app.application)
        flask_urls.register_urls(urls)
        result = self.test_app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_wrong_mapping_format_no_endpoint(self):
        from flask_url_mapping import FlaskUrls
        urls = [
            "/"
        ]
        with self.assertRaises(Exception) as context:
            flask_urls = FlaskUrls(self.test_app.application)
            flask_urls.register_urls(urls)
        self.assertTrue('Wrong mapping format!' in str(context.exception))

    def test_templates(self):
        from flask_url_mapping import FlaskUrls
        urls = [
            ("/home", "home.urls")
        ]
        flask_urls = FlaskUrls(self.test_app.application)
        flask_urls.register_urls(urls)

        result = self.test_app.get('/home/home_html')
        self.assertEqual(result.status_code, 200)

