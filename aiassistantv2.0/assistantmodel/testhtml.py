from django.test import TestCase

class SimpleTest(TestCase):
    def test_login(self):
        response = self.client.get('/login-post')
        self.assertEqual(response.status_code, 200)

