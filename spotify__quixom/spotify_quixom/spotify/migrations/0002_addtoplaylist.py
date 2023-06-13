# Generated by Django 4.2.1 on 2023-06-13 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("spotify", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AddToPlayList",
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
                (
                    "playlist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spotify.playlist",
                    ),
                ),
            ],
        ),
    ]
