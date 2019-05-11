from django.test import TestCase
#import unittest
from assistantmodel.models import Student
from django.test import Client

class SimpleTest(TestCase):
#class testhtml(unittest.TestCase):
    def test_login(self):
        response=self.client.get('/login-post')
        self.assertEqual(response.status_code,200)

'''if __name__=='__main__':
    unittest.main()'''