import factory
from factory.django import DjangoModelFactory
from factory import Faker
from django.contrib.auth import get_user_model
from spotify.models import  User, Singer, Song, Favourite, PlayList


class UserFactory(DjangoModelFactory):
    usernmae = Faker("user_name")
    email = Faker("email")
    role = Faker("singer")
    mobille_number = Faker("9874561230")
    password = Faker("password")

    class Meta:
        model = User


class SingerFactory(DjangoModelFactory):
    name = factory.Faker("singername")

    class Meta:
        model = Singer


class SongFactory(DjangoModelFactory):
    name = factory.Faker("song")
    singer = factory.SubFactory(SingerFactory)
    category = factory.Faker("category")

    class Meta:
        model = Song


class FavouriteFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    songs = factory.SubFactory(SongFactory)

    class Meta:
        model = Favourite


class PlayListFactory(DjangoModelFactory):
    name = factory.Faker("playlist")
    user = factory.SubFactory(UserFactory)
    songs = factory.SubFactory(SongFactory)

    class Meta:
        model = PlayList


class AddToPlayListFactory(DjangoModelFactory):
    playlist = factory.SubFactory(PlayListFactory)