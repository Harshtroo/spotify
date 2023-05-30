from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

class User(AbstractUser):
    "this model use create user"
    mobile_number = models.IntegerField(validators=[MaxValueValidator(9999999999)],default=0)

class Song(models.Model):
    """this model user create song"""
    ROLES=(
        ("English","English"),
        ("Gujrati","Gujrati"),
        ("Hindi","Hindi"),
    )
    name = models.CharField(max_length=100)
    singer_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50,choices=ROLES, null=True)