import factory
from factory.django import DjangoModelFactory
from factory import Faker
from django.contrib.auth import get_user_model
from spotify.models import  User, Singer, Song, Favourite, PlayList



class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    role = factory.Faker("singer")
    mobile_number = factory.Faker("9874561230")
    password = factory.Faker("password")

    class Meta:
        model = User


class SingerFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("singer")

    class Meta:
        model = Singer


class SongFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"song{n}")
    singer = factory.SubFactory(SingerFactory)
    category = factory.Faker("name")

    class Meta:
        model = Song


class FavouriteFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    songs = factory.Faker("word")

    class Meta:
        model = Favourite


class PlayListFactory(DjangoModelFactory):
    name = factory.Faker("name")
    user = factory.SubFactory(UserFactory)
    # songs = factory.RelatedFactory(
    #     SongFactory,
    #     factory_related_name='playlists',
    # )

    class Meta:
        model = PlayList

    @factory.post_generation
    def songs(self, create, extracted, **kwargs):
        print(create, extracted)
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for song in extracted:
                self.songs.add(song)

class AddToPlayListFactory(DjangoModelFactory):
    playlist = factory.SubFactory(PlayListFactory)