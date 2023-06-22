from django.test import TestCase, Client
from spotify.models import User,Singer,Song,Favourite,PlayList
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

    def test_all_field_required(self):
        with self.assertRaises(ValidationError):
            user = User.objects.create(email="abhi123@gmail.com", mobile_number=6355157752, role="singer")
            user.full_clean()
        with self.assertRaises(ValidationError):
            user = User.objects.create(username="abhi", mobile_number=6355157752, role="singer")
            user.full_clean()
        with self.assertRaises(ValidationError):
            user = User.objects.create(username="abhi1", email="abhi123@gmail.com", role="singer")
            user.full_clean()
        with self.assertRaises(ValidationError):
            user = User.objects.create(username="abhi2", email="abhi123@gmail.com", mobile_number=6355157752)
            user.full_clean()

    def test_create_user_with_invalid_mobile_number(self):
        with self.assertRaises(ValidationError) as context:
            user = User(mobile_number="123")
            user.full_clean()


    # TODO: For Required fields
    # TODO: Try to create test cases duplicate username
    # TODO: Normal create Success
    # TODO: Mobile number validation
    # TODO: Choose role choice which is not available ("Invalid")
    # TODO: ek user create usko is_active false kr diya baad me vapas us naam se create karne ka ??


class SingerTestCases(TestCase):

    def test_create_singer(self):
        singer = Singer.objects.create(name="Arijit singh")
        self.assertTrue(singer.name,"Arijit singh")


class CreateSongTestCases(TestCase):

    def test_create_new_song(self):
        singer = Singer.objects.create(name="Arijit singh")
        song = Song.objects.create(name="tum hi ho",singer=singer,category="Hindi")
        self.assertTrue(song.name, "tum hi ho")
        self.assertTrue(song.singer.name, "Arijit singh")
        self.assertTrue(song.category, "Hindi")

    def test_all_field_required(self):
        singer = Singer.objects.create(name="Arijit singh")
        with self.assertRaises(ValidationError):
            song = Song.objects.create(name="tum avo na",singer=singer)
            song.full_clean()
        with self.assertRaises(ValidationError):
            song = Song.objects.create(singer=singer,category="Hindi")
            song.full_clean()
        # with self.assertRaises(ValidationError):
        #     song = Song.objects.create(name="tum avo na",category="Hindi")
        #     song.full_clean()


class FavouriteTestCases(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="harsh")
        self.singer = Singer.objects.create(name="Arijit singh")
        self.song = Song.objects.create(name="tum hi ho",singer=self.singer,category="Hindi")

    def test_create_favourite(self):
        favourite = Favourite(user=self.user)
        try:
            favourite.full_clean()
            favourite.save()
            self.assertTrue(favourite.id)
        except Exception:
            pass

    def test_user_not_pass(self):
        favourite = Favourite.objects.create(songs=[self.song.id])
        try:

            self.assertTrue(favourite.id)
        except Exception as error:
            self.assertEqual(error,[""])
            pass


class TestPlayList(TestCase):
    def test_create_playlist(self):
        """
        To create playlist we need user, songs
        ...
        """
        user = User.objects.create(username="User1")
        singer = Singer.objects.create(name="Singer1")
        add_to_song = Song.objects.create(name="Song1",singer=singer, category="Hindi")
        playlist = PlayList.objects.create(name="Playlist1", user=user)
        playlist.songs.add(add_to_song.id)
        self.assertEqual(PlayList.objects.all().count(), 1)

    #     playlist.full_clean()
    #     playlist.save()
    #     self.assertTrue(playlist.id)

class AddToPlayListTestCases(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="harsh")
        self.singer = Singer.objects.create(name="Arijit singh")
        self.song = Song.objects.create(name="tum hi ho",singer=self.singer,category="Hindi")
        self.playlist=PlayList.objects.create(name="harshplaylist",user=self.user)

    def test_add_song_to_playlist(self):
        add_to_playlist = self.playlist
        song =Song.objects.create(name="tum hi ho",singer=self.singer,category="Hindi")
        add_to_playlist.songs.add(song.id)
        self.assertEqual(add_to_playlist.songs.first().id,song.id)




