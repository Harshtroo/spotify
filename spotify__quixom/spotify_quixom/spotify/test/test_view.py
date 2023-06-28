from django.test import TestCase, Client
from spotify.models import User, Singer, Song, Favourite, PlayList
from django.urls import reverse
from .factories import SongFactory, UserFactory, SingerFactory,FavouriteFactory,PlayListFactory,AddToPlayListFactory
from django.core.exceptions import ValidationError

class SongCreateTestCases(TestCase):

    def setUp(self):
        self.create_song_url = reverse("create_song")

    def test_create_song(self):
        song = SongFactory()

        song_data = {
            "name": song.name,
            "singer": song.singer.name,
            "category": song.category,
        }
        response = self.client.post(self.create_song_url, song_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Song.objects.count(), 1)
        self.assertEqual(Song.objects.first().name,song.name)


    def test_create_song_form_valid(self):
        song = SongFactory()

        song_data = {
            "name": song.name,
            "singer": song.singer,
            "category": song.category,
        }

        response = self.client.post(self.create_song_url, song_data)
        self.assertEqual(response.status_code, 200)

    def test_create_song_form_invalid(self):
        song = SongFactory()
        song_data = {
            "name": song.name,
            "singer": song.singer,
            "category": song.category,
        }
        response = self.client.post(self.create_song_url, song_data)
        self.assertEqual(response.status_code,200)


class SongListTestCases(TestCase):

    def setUp(self):
        self.song_list_url = reverse("song_list")

    def test_song_list(self):
        song = SongFactory()
        song_data = {
            "name": song.name,
            "singer": song.singer,
            "category": song.category,
        }
        response = self.client.get(self.song_list_url,song_data)
        self.assertEquals(response.status_code,302)
        self.assertTrue(Song.objects.filter(id=song.id).exists())


class SongUpdateTestCases(TestCase):

    def setUp(self):
        self.song = SongFactory()
        self.song_update_url = reverse("song_update", kwargs={"pk": self.song.id})

    def test_song_update(self):
        update_data = {
            "name": self.song.name,
            "singer": self.song.singer,
            "category": self.song.category,
        }
        response = self.client.post(self.song_update_url, update_data)
        self.assertEqual(200,response.status_code)
        self.song.refresh_from_db()
        self.assertEqual(self.song.name, self.song.name)


class SongDeleteTestCases(TestCase):

    def setUp(self):
        self.song = SongFactory()


    def test_song_delete(self):
        # song = SongFactory(name="song1", singer=self.song.singer, category="Hindi")
        response = self.client.post(reverse("song_delete", kwargs={"pk": self.song.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Song.objects.filter(id=self.song.id).exists())


class AddToFavouriteTestCases(TestCase):

    def setUp(self):
        self.favourite = FavouriteFactory()
        self.add_to_favourite_url = reverse("user_fav_song")

    def test_add_to_favourite_song(self):
        user = UserFactory()
        song = SongFactory()

        add_fav_data = {
            "user": user,
            "songs": song.id,
        }

        self.client.force_login(self.favourite.user)
        response = self.client.get(self.add_to_favourite_url, add_fav_data)
        print("responce ==========",response)
        # get_response = self.client.get(self.add_to_favourite_url)
        self.assertEqual(response.status_code, 200)
        # self.favourite.songs.set([self.favourite.songs.id])
        # self.assertTrue(Favourite.objects.filter(user=self.favourite.user, songs=song).exists())


class FavouriteListTestCases(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.favourite = FavouriteFactory(user=self.user)
        self.favourite_list_url = reverse("user_fav_song")

    def test_favourite_list_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.favourite_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.favourite, response.context["fav"])
        self.assertEqual(response.context["user"], self.user)


class CreatePlaylistTestCases(TestCase):

    def setUp(self):
        self.create_playlist_url = reverse("play_list")

    def test_create_playlist(self):
        user = UserFactory()
        song = SongFactory()
        playlist = PlayListFactory(user=user, songs=[song])

        playlist_data = {
            "name":  playlist.name,
            "user":  user.id,
        }

        response = self.client.post(self.create_playlist_url, playlist_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(PlayList.objects.filter(name=playlist.name).exists())

    def test_playlist_already_exists(self):
        create_playlist = PlayListFactory()
        song_ids = create_playlist.songs.values_list('id', flat=True)
        # create_playlist.songs.add(self.song)

        playlist_data = {
            "name": create_playlist.name,
            "songs": list(song_ids),
        }
        response = self.client.post(self.create_playlist_url, playlist_data)
        self.assertEqual(response.status_code, 200)


class ShowPlayListTestCases(TestCase):

    def setUp(self):
        self.user = UserFactory(username="testuser", password="testpassword")
        self.playlist = PlayListFactory(user=self.user)
        self.show_playlist_url = reverse("show_playlist")

    def test_show_playlist_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.show_playlist_url)
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, "show_play_list.html")
        self.assertEqual(response.context["user"], self.user)
        self.assertIn(self.playlist, response.context["playlist"])


class UpdatePlayListTestCases(TestCase):

    def setUp(self):
        self.user = UserFactory(username="testuser", password="testpassword")
        self.playlist = PlayListFactory(user=self.user, name="playlist1")
        self.update_playlist_url = reverse("update_playlist", kwargs={"pk": self.playlist.pk})
        self.form_data = {
            "name": "updated_playlist",
        }

    def test_update_playlist_view(self):
        self.client.force_login(self.user)
        response = self.client.post(self.update_playlist_url, self.form_data)
        self.assertEqual(200,response.status_code)
        self.playlist.refresh_from_db()
        self.assertTrue(PlayList.objects.filter(id=self.playlist.id).exists())


class DeletePlayListTestCases(TestCase):

    def setUp(self):
        self.user = UserFactory(username="testuser", password="testpassword")
        self.playlist = PlayListFactory(user=self.user, name="playlist1")
        self.delete_playlist_url = reverse("delete_playlist", kwargs={"pk": self.playlist.pk})

    def test_delete_playlist_view(self):
        self.client.force_login(self.user)
        response = self.client.post(self.delete_playlist_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("show_playlist"))
        self.assertFalse(PlayList.objects.filter(id=self.playlist.pk).exists())


class AddToPlaylistTestCases(TestCase):

    def setUp(self):
        self.user = UserFactory(username="testuser", password="testpassword")
        self.playlist = PlayListFactory(user=self.user, name="playlist1")
        self.singer = SingerFactory(name="singer1")
        self.song1 = SongFactory(name="song1", singer=self.singer)
        self.song2 = SongFactory(name="song2", singer=self.singer)
        self.add_to_playlist_url = reverse("add_song_playlist")

    def test_add_to_playlist_view(self):
        form_data = {
            "selected_ids[]": [self.song1.id, self.song2.id],
            "id_playlist": self.playlist.id,
        }
        self.client.force_login(self.user) 
        response = self.client.post(self.add_to_playlist_url, form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("show_playlist"))
        self.playlist.refresh_from_db()
        self.assertTrue(self.song1 in self.playlist.songs.all())
        self.assertTrue(self.song2 in self.playlist.songs.all())

    def test_add_to_playlist_view_no_song_selected(self):
        form_data = {
            "selected_ids[]": [],
            "id_playlist": self.playlist.id,
        }
        self.client.force_login(self.user) 
        response = self.client.post(self.add_to_playlist_url, form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("show_playlist"))
        self.playlist.refresh_from_db()
        self.assertFalse(self.playlist.songs.exists())

    def test_add_to_playlist_view_song_already_in_playlist(self):
        self.playlist.songs.add(self.song1)
        form_data = {
            "selected_ids[]": [self.song1.id],
            "id_playlist": self.playlist.id,
        }
        self.client.force_login(self.user) 
        response = self.client.post(self.add_to_playlist_url, form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("show_playlist"))
        self.playlist.refresh_from_db()
        self.assertEqual(self.playlist.songs.count(), 1)


class MulSongCreatePlaylistTestCases(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.singer = SingerFactory()
        self.song1 = SongFactory()
        self.song2 = SongFactory()
        self.playlist = PlayListFactory()
        self.create_playlist_url = reverse("mul_song_create_playlist")
        self.form_data = {
            "selected_ids[]": [self.song1.id, self.song2.id],
            "form": "My Playlist",
        }

    def test_create_playlist_view(self):
        self.client.force_login(self.playlist.user)
        response = self.client.post(self.create_playlist_url, self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("show_playlist"))
        self.assertTrue(PlayList.objects.filter(name="My Playlist", user=self.playlist.user).exists())

    def test_create_playlist_view_existing_playlist_name(self):
        self.client.force_login(self.user)
        playlist = PlayListFactory(user=self.user)
        # with self.assertRaises(ValidationError):
        response = self.client.post(self.create_playlist_url, self.form_data)
        self.assertEqual(response.status_code,302)
        self.assertTrue(PlayList.objects.filter(name=playlist.name, user=self.user).exists())


class RemovePlayListSongsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.playlist = PlayList.objects.create(name='My Playlist', user=self.user)
        self.singer = Singer.objects.create(name="singer1")
        self.song1 = Song.objects.create(name='Song 1',singer=self.singer)
        self.song2 = Song.objects.create(name='Song 2',singer=self.singer)
        self.playlist.songs.add(self.song1, self.song2)
        self.url = reverse('mul_remove_playlist')

    def test_remove_playlist_songs(self):
        self.client.force_login(self.user)

        data = {
            'selected_ids[]': [self.song1.id, self.song2.id],
            'id_playlist': self.playlist.id
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('show_playlist'))
        self.playlist.refresh_from_db()
        self.assertNotIn(self.song1, self.playlist.songs.all())
        self.assertNotIn(self.song2, self.playlist.songs.all())
#
    def test_remove_playlist_songs_invalid_playlist_id(self):
        self.client.force_login(self.user)

        data = {
            'selected_ids[]': [self.song1.id, self.song2.id],
            'id_playlist': 9999
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 404)

        self.playlist.refresh_from_db()
        self.assertIn(self.song1, self.playlist.songs.all())
        self.assertIn(self.song2, self.playlist.songs.all())

    def test_remove_playlist_songs_no_selected_songs(self):
        self.client.force_login(self.user)

        data = {
            'selected_ids[]': [],
            'id_playlist': self.playlist.id
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('show_playlist'))

        self.playlist.refresh_from_db()
        self.assertIn(self.song1, self.playlist.songs.all())
        self.assertIn(self.song2, self.playlist.songs.all())