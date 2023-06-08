from base.constance import Role
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.conf import settings


class User(AbstractUser):
    "this model use create user"
    mobile_number = models.IntegerField(validators=[MaxValueValidator(9999999999)], default=0)
    role = models.CharField(max_length=10, choices=Role.choices(), null=True)


class Singer(models.Model):
    """this models use create singer"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    """this model user create song"""

    ROLES = (
        ("English", "English"),
        ("Gujrati", "Gujrati"),
        ("Hindi", "Hindi"),
    )

    name = models.CharField(max_length=100)
    singer_name = models.ForeignKey(Singer, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=ROLES, null=True)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        '''soft delete function'''
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.name


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)


class PlayList(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

