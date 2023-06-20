from django.test import TestCase
from spotify.models import  User
from django.db import IntegrityError

class RegisterTestCases(TestCase):

    def test_registration_api(self):
        """ Test cases for successful registration"""
        user = User.objects.create_user(username="abhi", email="abhi123@gmail.com", mobile_number="6355157752", role="singer", password="abhi@1234")
        response = User.objects.get(username="abhi")
        self.assertEquals(response.username, user.username)

    def test_if_same_username_exist_return_400(self):
        """Test cases for incorrect username"""
        user = User.objects.create_user(username="abhi1", email="abhi123@gmail.com", mobile_number="6355157752", role="singer", password="abhi@1234")
        with self.assertRaises(IntegrityError) as context:
            User.objects.create(username="abhi1", email="abhi123@gmail.com", mobile_number="6355157752", role="singer", password="abhi@1234")

        self.assertTrue('UNIQUE constraint failed' in str(context.exception))

    def test_all_field_required_or_return_400(self):
        user = User(mobile_number="6355157752", role="singer", password="abhi@1234")
        try:
            user.full_clean()
        except Exception as e:
            assert dict(e).get("username")== ['This field cannot be blank.']
    #
