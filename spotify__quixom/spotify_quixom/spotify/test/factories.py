from factory.django import DjangoModelFactory
from factory import Faker
from django.contrib.auth import get_user_model


class UserFactory(DjangoModelFactory):
    usernmae = Faker("user_name")
    email = Faker("email")
    role = Faker("singer")
    mobille_number = Faker("9874561230")
    password = Faker("password")

    class Meta:
        model = get_user_model()
