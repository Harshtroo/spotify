from django.test import TestCase, Client
from spotify.models import User, Singer, Song, Favourite, PlayList
from django.urls import reverse

# class SongCreateTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.create_user_url = reverse("create_song")
#
#     def test_create_song(self):
#         self.singer1 = Singer.objects.create(name="singer1")
#         user = User.objects.create(username="testuser",password="1234")
#         self.client.force_login(user)
#         song_data = {
#             "name": "Tum Hi Ho",
#             "singer": "Arijit Singh",
#             "category": "Hindi",
#         }
#         song = Song.objects.create(name="song1",singer=self.singer1,category="Hindi")
#         response = self.client.post(self.create_user_url, song_data)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(Song.objects.count(), 1)
#         self.assertEqual(Song.objects.first().name, "song1")
#
#     def test_create_song_form_valid(self):
#         song_data = {
#                     "name": "song1",
#                     "singer": "singer1",
#                     "category": "Hindi",
#                 }
#         response = self.client.post(self.create_user_url,song_data)
#         self.assertEqual(response.status_code, 200)
#         # self.assertRedirects(reverse("home"))
#
#     def test_create_song_form_invalid(self):
#         song_data = {
#                     "name": "song1",
#                     "category": "Hindi",
#                 }
#         response = self.client.post(self.create_user_url, song_data)
#         self.assertEqual(response.status_code,200)


# class SongListTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.singer1 = Singer.objects.create(name="singer1")
#         self.singer2 = Singer.objects.create(name="singer2")
#         self.song_list_url = reverse("song_list")
#         self.song1 = Song.objects.create(name="song1",singer=self.singer1,category="Hindi")
#         song2 = Song.objects.create(name="song2",singer=self.singer2,category="Hindi")
#
#     def test_song_list(self):
#         response = self.client.get(self.song_list_url)
#         # print("response==========",response.content["song_id_list"])
#         self.assertIn(self.song1,response.content["song_id_list"])

#
# class SongUpdateTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.song_update_url = reverse("song_update")
#         self.singer1 = Singer.objects.create(name="singer1")
#         self.song1 = Song.objects.create(name="song1",singer=self.singer1,category="Hindi")
#
#     def test_song_update(self):
#         # song = self.song1
#         print("song==========================",self.song1)
        # update_url = reverse(
        #     "song_update",kwargs={"pk":song.id}
        # )
#         update_data={
#             "name":"song2",
#             "singer":self.singer1,
#             "category":"Hindi"
#         }
#         response = self.client.post(update_url,update_data),
#         print("responce ==============",response)
#         # self.assertEqual(response.status_code == 302)
#         self.assertEqual(song.name, 'song2')


# class SongDeleteTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.singer1 = Singer.objects.create(name="singer1")
#         # self.song = Song.objects.create(name="song1",singer=self.singer1,category="Hindi")
#
#     def test_song_delete(self):
#         song = Song.objects.create(name="song1", singer=self.singer1, category="Hindi")
#         response = self.client.post(reverse("song_delete",kwargs={"pk":song.id}))
#         self.assertEqual(response.status_code,302)

#
# class AddToFavouriteTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.singer1 = Singer.objects.create(name="singer1")
#         self.song = Song.objects.create(name="song1", singer=self.singer1, category="Hindi")
#
#     def test_add_to_favourite_song(self):
#         user1 = User.objects.create(username="testuser", password="1234")
#         print("user1==============",user1)
#         user = self.client.force_login(user1)
#         print("user========",user)
#
#         fav_song = Favourite.objects.create(user=user1, songs=self.song)
        # response = self.client.post(reverse("song_fav"), fav_song)
        # print("response=============",response)


class CreatePlaylistTestCases(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_playlist_url = reverse("play_list")
        self.singer1 = Singer.objects.create(name="singer1")
        self.song = Song.objects.create(name="song1", singer=self.singer1, category="Hindi")
        self.playlist = PlayList.objects.create(name="playlist1",songs=self.song)

    def test_create_playlist(self):
        playlist_data = {
            "name":"playlist12",
            "songs":"song12"
        }
        response = self.client.post(self.create_playlist_url,playlist_data)
        self.assertEqual(response.status_code,200)