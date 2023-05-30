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
]