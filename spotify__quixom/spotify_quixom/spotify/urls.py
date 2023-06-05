from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from spotify import views

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('login/',views.Login.as_view(),name="login"),
    path('logout/',views.Logout.as_view(),name="logout"),
    path('singup/',views.SingUp.as_view(),name="singup"),
    path('create_song/',views.SongCreate.as_view(),name="create_song"),
    path('song_list/',views.SongList.as_view(),name="song_list"),
    path('song_update/<int:pk>',views.SongUpdate.as_view(),name="song_update"),
    path('song_delete/<int:pk>',views.SongDelete.as_view(),name="song_delete"),
    path('song_fav/<int:pk>',views.AddToFavourite.as_view(),name="song_fav"),
]   