from django.test import TestCase, Client
from spotify.models import User
from django.urls import reverse
from django.test import RequestFactory
from spotify.views import SongCreate

class CreateSongTestCases(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.create_user_url = reverse("create_song")

    def test_create_song(self):
        user = User.objects.create(username="testuser")
        song_data={
            "name": "Tum Hi Ho",
            "singer": "Arijit Singh",
            "category": "Hindi",
        }
        request = self.factory.post(self.create_user_url,song_data)
        request.user =user
        response = SongCreate.as_view()(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Song.objects.count(), 1)
        self.assertEqual(Song.objects.first().name, "Tum Hi Ho")

