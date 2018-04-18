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
        from flask_url_mapping import register_urls
        from test.testapp import views
        urls = [
            ("/", views.index, ["GET"]),
        ]
        register_urls(self.test_app.application, urls)
        result = self.test_app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_users(self):
        from flask_url_mapping import register_urls
        from test.testapp import views
        urls = [
            ("/users", views.get_users, ["GET"]),
        ]
        register_urls(self.test_app.application, urls)
        result = self.test_app.get('/users')
        self.assertEqual(result.status_code, 200)

    def test_home_index(self):
        from flask_url_mapping import register_urls
        urls = [
            ("/home", "home.urls")
        ]
        register_urls(self.test_app.application, urls)
        result = self.test_app.get('/home/home_index')
        self.assertEqual(result.status_code, 200)

    def test_home_users(self):
        from flask_url_mapping import register_urls
        urls = [
            ("/home", "home.urls")
        ]
        register_urls(self.test_app.application, urls)
        result = self.test_app.get('/home/home_users')
        self.assertEqual(result.status_code, 200)

    def test_blueprint(self):
        from test.testapp.blueprints.bp1.views import bp1
        self.test_app.application.register_blueprint(bp1)
        result = self.test_app.get('/bp1')
        self.assertEqual(result.status_code, 200)

    def test_missing_http_method(self):
        from flask_url_mapping import register_urls
        from test.testapp import views
        urls = [
            ("/", views.index),
        ]
        register_urls(self.test_app.application, urls)
        result = self.test_app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_wrong_mapping_format(self):
        from flask_url_mapping import register_urls
        urls = [
            "/"
        ]
        with self.assertRaises(Exception) as context:
            register_urls(self.test_app.application, urls)

        self.assertTrue('Wrong mapping format!' in str(context.exception))


