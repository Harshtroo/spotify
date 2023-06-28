import factory
from factory.django import DjangoModelFactory
from factory import Faker
from django.contrib.auth import get_user_model
from spotify.models import  User, Singer, Song, Favourite, PlayList


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    role = factory.Faker("name")
    mobile_number = factory.Faker("random_number", digits=10)
    password = factory.Faker("password")

    class Meta:
        model = User


class SingerFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = Singer


class SongFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"song{n}")
    singer = factory.SubFactory(SingerFactory)
    category = factory.Faker("name")

    class Meta:
        model = Song


class FavouriteFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    # songs = factory.Faker("word")

    class Meta:
        model = Favourite

    @factory.post_generation
    def songs(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of songs was passed in, use them
            for song in extracted:
                self.songs.set(song)
class PlayListFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = PlayList

    @factory.post_generation
    def songs(self, create, extracted, **kwargs):

        if not create:
            return
        if extracted:
            for song in extracted:
                self.songs.add(song)

class AddToPlayListFactory(DjangoModelFactory):
    playlist = factory.SubFactory(PlayListFactory)