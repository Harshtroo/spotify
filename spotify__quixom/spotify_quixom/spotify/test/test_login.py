from django.test import TestCase, Client
from spotify.models import User


class LoginTestCases(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="abhi",
                                             email="abhi123@gmail.com",
                                             mobile_number="6355157752",
                                             role="singer",
                                             password="abhi@1234")

    def test_user_login_success(self):
        response = self.client.post('/login/', {'username': 'abhi', 'password': 'abhi@1234'})
        self.assertEqual(response.status_code, 302)  # 302 requested page has moved temporarily to a new url
        self.assertRedirects(response, '/')

    def test_user_login_failure(self):
        response = self.client.post('/login/', {
            'username': 'abhi',
            'password': 'wrong_password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        self.client.force_login(self.user)
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)  # Check if the logout is successful
        self.assertRedirects(response, '/login/')