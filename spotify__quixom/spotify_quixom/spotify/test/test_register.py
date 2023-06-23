from django.test import TestCase,Client
from spotify.models import User
from django.urls import reverse

class RegisterTestCases(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("singup")


    def test_registration_api(self):
        """ Test cases for successful registration"""
        data = {"username":"abhi",
             "email":"abhi123@gmail.com",
             "mobile_number":"6355157752",
             "role":"singer",
             "password":"abhi@1234"
        }
        response = self.client.post(self.url,data)
        self.assertEqual(response.status_code,200)


    def test_all_field_required_or_return_400(self):
        user = User(mobile_number="6355157752", role="singer", password="abhi@1234")
        with self.assertRaises(Exception) as e:
            user.full_clean()
        self.assertEqual(dict(e.exception)['username'], ['This field cannot be blank.'])

