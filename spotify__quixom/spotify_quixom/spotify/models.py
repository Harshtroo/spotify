from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    "this model use create user"
    username = models.CharField(max_length=100,unique=True)

class Song(models.Model):
    ROLES=(
        ("English","English"),
        ("Gujrati","Gujrati"),
        ("Hindi","Hindi"),
    )
    name = models.CharField(max_length=100)
    singer_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50,choices=ROLES, null=True)