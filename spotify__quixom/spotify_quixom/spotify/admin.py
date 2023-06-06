from django.contrib import admin
from .models import User,Song,Singer,Favorite

admin.site.register(User)
admin.site.register(Singer)
admin.site.register(Song)
admin.site.register(Favorite)
