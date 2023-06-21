from django.test import TestCase, Client
from spotify.models import User
from django.core.exceptions import ValidationError

class UserTstCases(TestCase):

    def test_create_user(self):
        user = User.objects.create(username="abhi",email="abhi123@gmail.com",mobile_number=6355157752,role="singer")
        user.set_password("abhi@1234")  
        user.save()
        self.assertEqual(user.username, "abhi")
        self.assertEqual(user.email, "abhi123@gmail.com")
        self.assertEqual(user.mobile_number, 6355157752)  
        self.assertEqual(user.role, "singer")
        self.assertTrue(user.check_password("abhi@1234"))

    # def test_all_field_required(self):
    #     with self.assertRaises(ValidationError):
    #         user = User.objects.create(email="abhi123@gmail.com", mobile_number=6355157752, role="singer")

    #     with self.assertRaises(ValidationError):
    #         user = User.objects.create(username="abhi", mobile_number=6355157752, role="singer")

    #     with self.assertRaises(ValidationError):
    #         user = User.objects.create(username="abhi", email="abhi123@gmail.com", role="singer")

    #     with self.assertRaises(ValidationError):
    #         user = User.objects.create(username="abhi", email="abhi123@gmail.com", mobile_number=6355157752)

    def test_create_user_with_invalid_mobile_number(self):
        with self.assertRaises(ValidationError) as context:
            User.objects.create(username='abhi', mobile_number="123", role='singer')
        self.assertEqual(context.exception.message_dict['mobile_number'][0], 'Ensure this value is greater than or equal to 0 and less than or equal to 9999999999.')

    # def test_mobile_number_validator(self):
    #     # Test the mobile number validator
    #     with self.assertRaises(ValidationError):
    #         user = User(
    #             username="abhi",
    #             email="abhi123@gmail.com",
    #             mobile_number=123456789,  # Invalid mobile number, less than 10 digits
    #             role="singer",
    #             password="abhi@1234"
    #         )
    #         user.full_clean()  




    # def test_required_fields(self):
    #     # user = User.objects.create(username="abhi",email="abhi@gmail.com",mobile_number="9874561230",role="singer",password="harsh@1234")
    #     user = User(username="abhi")
    #     # with self.assertRaises(ValidationError):



    # TODO: For Required fields
    # TODO: Try to create test cases duplicate username
    # TODO: Normal create Success
    # TODO: Mobile number validation
    # TODO: Choose role choice which is not available ("Invalid")
    # TODO: ek user create usko is_active false kr diya baad me vapas us naam se create karne ka ??



# class CreateSongTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.create_song_url = reverse("create_song")
#         self.create_song = Song.objects.create(name="suno", singer_name="arijit singh", category="Hindi")
#
#     def User_create_new_song(self):
#         response = self.client.post(self.create_song_url, self.create_song)
#         self.assertEquals(response.status_code, 302)
#         self.assertRedirects(response, "/song_list/")
#
#     # def test_all_field_required_or_return_400(self):
#     #     song_data = Song(name="suno", category="Hindi")
#     #     with self.assertRaises(Exception) as e:
#     #         song_data.full_clean()
#     #     self.assertEqual(dict(e.exception)['singer_name'], ['This field cannot be blank.'])
