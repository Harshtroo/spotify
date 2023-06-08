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
    path('song_fav/',views.AddToFavourite.as_view(),name="song_fav"),
    path('user_fav_song/',views.LoginUserFavouriteSong.as_view(),name="user_fav_song"),
    path('play_list/',views.CreatePlayList.as_view(),name="play_list"),
    path('show_playlist/',views.ShowPlayList.as_view(),name="show_playlist"),
    path('update_playlist/<int:pk>',views.UpdatePlayList.as_view(),name="update_playlist"),
    path('delete_playlist/<int:pk>',views.DeletePlayList.as_view(),name="delete_playlist"),
]   