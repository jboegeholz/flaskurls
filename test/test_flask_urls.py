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
        result = self.test_app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_users(self):
        result = self.test_app.get('/users')
        self.assertEqual(result.status_code, 200)






