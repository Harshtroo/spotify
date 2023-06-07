from typing import Any, Dict, Optional, Type
from django.db import models
from django.forms.forms import BaseForm
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .form import SignUpForm, LoginForm, SongForm, CreatePlayListForm
from .models import User, Song, Favourite, PlayList
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.models import Group, Permission
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

class Home(TemplateView):
    """ Home page view """
    template_name = "home.html"


class Login(LoginView):
    """ Login page view"""
    form_class = LoginForm
    template_name ="login.html"
    success_url =reverse_lazy("home")


class Logout(LogoutView):
    """logout class"""
    pass


class SingUp(CreateView):
    """ SignUp page view """
    model = User
    template_name = "sing_up.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            user = form.save()
            user.save()
            user_role = user.role
            group = Group.objects.get(name=user_role)
            user.groups.add(group.id)
            return HttpResponseRedirect(self.success_url)
        return render(request,"sing_up.html",{"form":form})


class SongCreate(SuccessMessageMixin,CreateView):
    template_name = "create_song.html"
    form_class = SongForm
    success_url = reverse_lazy("home")
    success_message = "successfully create song"

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            super(SongCreate,self).post(request, *args, **kwargs)
            return redirect(self.success_url)
        return render(request,self.template_name,{"form":form})


class SongList(ListView):
    model = Song
    template_name = "song_list.html"
    context_object_name = 'song'
    queryset = Song.objects.filter(is_deleted = False)
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        song_obj = Favourite.objects.get(user=self.request.user)
        song_id_list = []
        for song in song_obj.songs.all():
            song_id_list.append(song.id)
        context["song_id_list"] = song_id_list
        return context


class SongUpdate(SuccessMessageMixin,UpdateView):
    """ song updatge view """
    model =  Song
    form_class = SongForm
    template_name = "create_song.html"
    success_url = reverse_lazy('song_list')
    success_message = "successfully edit song"

    def post(self, request, *args, **kwargs):
            form = self.form_class(self.request.POST or None)
            if form.is_valid():
                super(SongUpdate,self).post(request, *args, **kwargs)
                return redirect(self.success_url)
            return render(request,self.template_name,{"form":form})


class SongDelete(SuccessMessageMixin,DeleteView):
    """ song delete view """
    model = Song
    success_url = reverse_lazy("song_list")
    success_message = "successfully delete song"

    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist('checkbox_ids[]')
        if selected_ids:
            Song.objects.filter(id__in=selected_ids).update(is_deleted = True)
            messages.success(request, self.success_message)
        return JsonResponse({"messages":"success"})


class AddToFavourite(CreateView):
    """ song add to favourite """
    model = Favourite

    def post(self, request, *args, **kwargs):
        song_id = self.request.POST.get('song_id')
        obj, create = Favourite.objects.get_or_create(user=self.request.user)
        if obj.songs.filter(id=song_id).exists():
            obj.songs.remove(Song.objects.get(id=song_id))
            context = {
                "status": True,
                "message": "Song Removed!",
                "song_id": song_id
            }
        else:
            obj.songs.add(Song.objects.get(id=song_id))
            context = {
                "status": True,
                "message": "Song Added!",
                "song_id": song_id
            }
        obj.save()
        return JsonResponse(context)


class LoginUserFavouriteSong(ListView):
    model = Favourite
    template_name = 'favorite_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['fav'] = Favourite.objects.filter(user=self.request.user)
        return context


class CreatePlayList(SuccessMessageMixin,CreateView):
    form_class = CreatePlayListForm
    template_name = "play_list.html"
    success_url = reverse_lazy("song_list")
    success_message = "successfully create playlist"

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            form.save()
            return redirect(self.success_url)
        return render(request,self.template_name,{"form":form})


class ShowPlayList(ListView):
    model = PlayList
    template_name = "show_play_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['playlist'] = PlayList.objects.filter(user=self.request.user)
        # breakpoint()
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     context['fav'] = Favourite.objects.filter(user=self.request.user)
    #     return context