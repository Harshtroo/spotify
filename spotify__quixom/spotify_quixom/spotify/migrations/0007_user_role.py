# Generated by Django 4.2.1 on 2023-05-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spotify", "0006_alter_user_password_alter_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("student", "student"), ("librarian", "librarian")],
                max_length=10,
                null=True,
            ),
        ),
    ]