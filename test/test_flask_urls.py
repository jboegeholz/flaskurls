import unittest
from test.testapp.application import create_app

class FlaskUrlsTest(unittest.TestCase):
    def setUp(self):
        # creates testapp under test
        self.app_under_test = create_app().test_client()
        self.app_under_test.testing = True

    def tearDown(self):
        pass

    def test_root(self):
        result = self.app_under_test.get('/')
        self.assertEqual(result.status_code, 200)

    def test_users(self):
        result = self.app_under_test.get('/users')
        self.assertEqual(result.status_code, 200)






