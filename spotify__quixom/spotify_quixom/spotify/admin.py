from django.contrib import admin
from .models import User,Song,Singer,Favourite,PlayList

admin.site.register(User)
admin.site.register(Singer)
admin.site.register(Song)
admin.site.register(Favourite)
admin.site.register(PlayList)
