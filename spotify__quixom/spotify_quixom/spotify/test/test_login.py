from django.test import TestCase
from spotify.models import User
from django.test import Client

class LoginTestCases(TestCase):

    def user_login(self):
        user = User.objects.create_user(username="abhi", email="abhi123@gmail.com", mobile_number="6355157752", role="singer", password="abhi@1234")
        user.save()
        user_clint = Client()
        login = user_clint.login(username="deep",password="deep@1234")
        self.assertEquals(login.status_code,201)
        print("user=====",user)

