from django.test import TestCase, Client,RequestFactory
from spotify.models import User, Singer, Song, Favourite, PlayList
from django.urls import reverse
from .factories import SongFactory, UserFactory

class SongCreateTestCases(TestCase):

    def setUp(self):
        self.factory = SongFactory
        # self.create_user_url = reverse("create_song")

    def test_create_song(self):
        self.singer1 = Singer.objects.create(name="singer1")
        user = UserFactory

        song_data = {
            "name": "Tum Hi Ho",
            "singer": "Arijit Singh",
            "category": "Hindi",
        }
        song = Song.objects.create(name="song1",singer=self.singer1,category="Hindi")
        response = self.factory.post(self.create_user_url, song_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Song.objects.count(), 1)
        self.assertEqual(Song.objects.first().name, "song1")

    # def test_create_song_form_valid(self):
    #     song_data = {
    #                 "name": "song1",
    #                 "singer": "singer1",
    #                 "category": "Hindi",
    #             }
    #     response = self.client.post(self.create_user_url,song_data)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertRedirects(response,reverse("song_list"))

    # def test_create_song_form_invalid(self):
    #     song_data = {
    #                 "name": "song1",
    #                 "category": "Hindi",
    #             }
    #     response = self.client.post(self.create_user_url, song_data)
    #     self.assertEqual(response.status_code,200)


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
#     # def test_song_list(self):
#     #     response = self.client.get(self.song_list_url)
#     #     self.assertEqual(response.status_code, 302)
#     #     # self.assertEqual(response.status_code, 200)
#     #     self.assertContains(response, self.song1.name)
#     #     self.assertContains(response, self.song2.name)
#
# class SongUpdateTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         # self.song_update_url = reverse("song_update")
#         self.singer1 = Singer.objects.create(name="singer1")
#         self.song1 = Song.objects.create(name="song1",singer=self.singer1,category="Hindi")
#         self.song_update_url = reverse("song_update", kwargs={"pk": self.song1.id})
#
#     def test_song_update(self):
#         # update_url = reverse(
#         #     "song_update",kwargs={"pk":song.id}
#         # )
#         update_data={
#             "name":"song2",
#             "singer":self.singer1.id,
#             "category":"Hindi"
#         }
#         response = self.client.post(self.song_update_url, update_data)
#         self.assertEqual(response.status_code, 302)
#         self.song1.refresh_from_db()
#         self.assertEqual(self.song1.name, "song2")
#
#
# # class SongDeleteTestCases(TestCase):
# #
# #     def setUp(self):
# #         self.client = Client()
# #         self.singer1 = Singer.objects.create(name="singer1")
# #
# #     def test_song_delete(self):
# #         song = Song.objects.create(name="song1", singer=self.singer1, category="Hindi")
# #         response = self.client.delete(reverse("song_delete", kwargs={"pk": song.id}))
# #         self.assertEqual(response.status_code, 302)
# #         self.assertFalse(Song.objects.filter(id=song.id).exists())
#
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
#         user = self.client.force_login(user1)
#         response = self.client.post(reverse("song_fav"), {"song_id": self.song.id})
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue(Favourite.objects.filter(user=user1, songs=self.song).exists())
#
#
# class FavouriteListTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create(username="testuser", password="testpassword")
#         self.favourite = Favourite.objects.create(user=self.user)
#         self.favourite_list_url = reverse("user_fav_song")
#
#     def test_favourite_list_view(self):
#         self.client.force_login(self.user)
#         response = self.client.get(self.favourite_list_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(self.favourite, response.context["fav"])
#         self.assertEqual(response.context["user"], self.user)
#
#
# class CreatePlaylistTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.create_playlist_url = reverse("play_list")
#         self.singer1 = Singer.objects.create(name="singer1")
#         self.song = Song.objects.create(name="song1", singer=self.singer1, category="Hindi")
#         self.user = User.objects.create(username="testuser", password="testpassword")
#         self.client.force_login(self.user)
#
#     def test_create_playlist(self):
#         playlist_data = {
#             "name": "playlist12",
#             "songs": [self.song.id],
#         }
#         response = self.client.post(self.create_playlist_url, playlist_data)
#         self.assertEqual(response.status_code, 302)
#         self.assertTrue(PlayList.objects.filter(name="playlist12").exists())
#
#     def test_Playlist_already_exists(self):
#         create_playlist = PlayList.objects.create(name="playlist",user=self.user)
#         create_playlist.songs.add(self.song.id)
#         playlist_data = {
#             "name": "playlist",
#             "songs": [self.song.id],
#         }
#         response = self.client.post(self.create_playlist_url,playlist_data)
#         self.assertEqual(response.status_code,200)
#
#
# class ShowPlayListTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create(username="testuser", password="testpassword")
#         self.playlist = PlayList.objects.create(user=self.user)
#         self.show_playlist_url = reverse("show_playlist")
#
#     def test_show_playlist_view(self):
#         self.client.force_login(self.user)
#         response = self.client.get(self.show_playlist_url)
#         self.assertEqual(response.status_code, 200)
#         # self.assertTemplateUsed(response, "show_play_list.html")
#         self.assertEqual(response.context["user"], self.user)
#         self.assertIn(self.playlist, response.context["playlist"])
#
#
# # class UpdatePlayListTestCases(TestCase):
# #     def setUp(self):
# #         self.client = Client()
# #         self.user = User.objects.create(username="testuser", password="testpassword")
# #         self.playlist = PlayList.objects.create(user=self.user, name="playlist1")
# #         self.update_playlist_url = reverse("update_playlist", kwargs={"pk": self.playlist.pk})
# #         self.form_data = {
# #             "name": "updated_playlist",
# #         }
# #
# #     def test_update_playlist_view(self):
# #         self.client.force_login(self.user)
# #         response = self.client.post(self.update_playlist_url, self.form_data)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertRedirects(response, reverse("show_playlist"), target_status_code=302)
# #         self.playlist.refresh_from_db()
# #         self.assertEqual(self.playlist.name, "updated_playlist")
#
#
# class DeletePlayListTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create(username="testuser", password="testpassword")
#         self.playlist = PlayList.objects.create(user=self.user, name="playlist1")
#         self.delete_playlist_url = reverse("delete_playlist", kwargs={"pk": self.playlist.pk})
#
#     def test_delete_playlist_view(self):
#         self.client.force_login(self.user)
#         response = self.client.post(self.delete_playlist_url)
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse("show_playlist"))
#         self.assertFalse(PlayList.objects.filter(id=self.playlist.pk).exists())
#
#
# class AddToPlaylistTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create(username="testuser", password="testpassword")
#         self.playlist = PlayList.objects.create(user=self.user, name="playlist1")
#         self.singer = Singer.objects.create(name="singer1")
#         self.song1 = Song.objects.create(name="song1",singer=self.singer)
#         self.song2 = Song.objects.create(name="song2",singer=self.singer)
#         self.add_to_playlist_url = reverse("add_song_playlist")
#
#     def test_add_to_playlist_view(self):
#         self.client.force_login(self.user)
#         form_data = {
#             "selected_ids[]": [self.song1.id, self.song2.id],
#             "id_playlist": self.playlist.id,
#         }
#         response = self.client.post(self.add_to_playlist_url, form_data)
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse("show_playlist"))
#         self.playlist.refresh_from_db()
#         self.assertTrue(self.song1 in self.playlist.songs.all())
#         self.assertTrue(self.song2 in self.playlist.songs.all())
#
#     def test_add_to_playlist_view_no_song_selected(self):
#         self.client.force_login(self.user)
#         form_data = {
#             "selected_ids[]": [],
#             "id_playlist": self.playlist.id,
#         }
#         response = self.client.post(self.add_to_playlist_url, form_data)
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse("show_playlist"))
#         self.playlist.refresh_from_db()
#         self.assertFalse(self.playlist.songs.exists())
#
#     def test_add_to_playlist_view_song_already_in_playlist(self):
#         self.client.force_login(self.user)
#         self.playlist.songs.add(self.song1)
#         form_data = {
#             "selected_ids[]": [self.song1.id],
#             "id_playlist": self.playlist.id,
#         }
#         response = self.client.post(self.add_to_playlist_url, form_data)
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse("show_playlist"))
#         self.playlist.refresh_from_db()
#         self.assertEqual(self.playlist.songs.count(), 1)
#
#
# class MulSongCreatePlaylistTestCases(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create(username="testuser", password="testpassword")
#         self.singer = Singer.objects.create(name="singer1")
#         self.song1 = Song.objects.create(name="song1",singer=self.singer)
#         self.song2 = Song.objects.create(name="song2",singer=self.singer)
#         self.create_playlist_url = reverse("mul_song_create_playlist")
#         self.form_data = {
#             "selected_ids[]": [self.song1.id, self.song2.id],
#             "form": "My Playlist",
#         }
#
#     def test_create_playlist_view(self):
#         self.client.force_login(self.user)
#         response = self.client.post(self.create_playlist_url, self.form_data)
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse("show_playlist"))
#         self.assertTrue(PlayList.objects.filter(name="My Playlist", user=self.user).exists())
#
#     # def test_create_playlist_view_existing_playlist_name(self):
#     #     self.client.force_login(self.user)
#     #     playlist = PlayList.objects.create(name="My Playlist", user=self.user)
#     #     with self.assertRaises(ValidationError):
#     #         response = self.client.post(self.create_playlist_url, self.form_data)
#     #     self.assertFalse(PlayList.objects.filter(name="My Playlist", user=self.user).exists())
#
#
# class RemovePlayListSongsTestCase(TestCase):
#
#     def setUp(self):
#         self.user = User.objects.create(username='testuser')
#         self.playlist = PlayList.objects.create(name='My Playlist', user=self.user)
#         self.singer = Singer.objects.create(name="singer1")
#         self.song1 = Song.objects.create(name='Song 1',singer=self.singer)
#         self.song2 = Song.objects.create(name='Song 2',singer=self.singer)
#         self.playlist.songs.add(self.song1, self.song2)
#         self.url = reverse('mul_remove_playlist')
#
#     def test_remove_playlist_songs(self):
#         self.client.force_login(self.user)
#
#         data = {
#             'selected_ids[]': [self.song1.id, self.song2.id],
#             'id_playlist': self.playlist.id
#         }
#         response = self.client.post(self.url, data)
#
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, reverse('show_playlist'))
#         self.playlist.refresh_from_db()
#         self.assertNotIn(self.song1, self.playlist.songs.all())
#         self.assertNotIn(self.song2, self.playlist.songs.all())
#
#     def test_remove_playlist_songs_invalid_playlist_id(self):
#         self.client.force_login(self.user)
#
#         data = {
#             'selected_ids[]': [self.song1.id, self.song2.id],
#             'id_playlist': 9999
#         }
#         response = self.client.post(self.url, data)
#
#         self.assertEqual(response.status_code, 404)
#
#         self.playlist.refresh_from_db()
#         self.assertIn(self.song1, self.playlist.songs.all())
#         self.assertIn(self.song2, self.playlist.songs.all())
#
#     def test_remove_playlist_songs_no_selected_songs(self):
#         self.client.force_login(self.user)
#
#         data = {
#             'selected_ids[]': [],
#             'id_playlist': self.playlist.id
#         }
#         response = self.client.post(self.url, data)
#
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, reverse('show_playlist'))
#
#         self.playlist.refresh_from_db()
#         self.assertIn(self.song1, self.playlist.songs.all())
#         self.assertIn(self.song2, self.playlist.songs.all())