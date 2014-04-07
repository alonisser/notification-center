import unittest
import webapp2
import webtest
from main import APIHandler


class TestAPIHandler(unittest.TestCase):
    def setUp(self):
        app = webapp2.WSGIApplication(['/', APIHandler])
        self.testapp = webtest(app)

    def test_returns_ok_for_get(self):

        response = self.testapp.get('/')
        self.assertEqual(response.status_int, 200)