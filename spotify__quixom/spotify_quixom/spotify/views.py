from typing import Any, Dict, Optional, Type
from django.db import models
from django.forms.forms import BaseForm
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .form import SignUpForm,LoginForm,SongForm
from .models import User,Song
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.models import Group, Permission
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect

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

    def get_queryset(self):
        queryset = Song.objects.all()
        return queryset


class SongUpdate(SuccessMessageMixin,UpdateView):
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
    model = Song
    template_name = "create_song.html"
    success_url = reverse_lazy("song_list")
    success_message = "successfully delete song"