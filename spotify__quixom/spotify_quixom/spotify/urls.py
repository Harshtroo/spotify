from django.urls import path
from spotify import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("singup/", views.SingUp.as_view(), name="singup"),
    path("create_song/", views.SongCreate.as_view(), name="create_song"),
    path("song_list/", views.SongList.as_view(), name="song_list"),
    path("song_update/<int:pk>", views.SongUpdate.as_view(), name="song_update"),
    path("song_delete/", views.SongDelete.as_view(), name="song_delete"),
    path("song_fav/", views.AddToFavourite.as_view(), name="song_fav"),
    path("user_fav_song/", views.FavouriteList.as_view(), name="user_fav_song"),
    path("play_list/", views.CreatePlayList.as_view(), name="play_list"),
    path("show_playlist/", views.ShowPlayList.as_view(), name="show_playlist"),
    path("update_playlist/<int:pk>",views.UpdatePlayList.as_view(),name="update_playlist"),
    path("delete_playlist/<int:pk>",views.DeletePlayList.as_view(),name="delete_playlist"),
    path("add_song_playlist/", views.AddToPlaylist.as_view(), name="add_song_playlist"),
    path("mul_song_create_playlist/",views.MulSongCreatePlaylist.as_view(),name="mul_song_create_playlist"),
    path("mul_remove_playlist/",views.RemovePlayListSongs.as_view(),name="mul_remove_playlist"),
]
