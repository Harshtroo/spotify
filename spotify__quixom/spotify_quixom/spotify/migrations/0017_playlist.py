# Generated by Django 4.2.1 on 2023-06-07 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("spotify", "0016_rename_favorite_favourite"),
    ]

    operations = [
        migrations.CreateModel(
            name="PlayList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("list_name", models.CharField(max_length=100)),
                ("songs", models.ManyToManyField(to="spotify.song")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
