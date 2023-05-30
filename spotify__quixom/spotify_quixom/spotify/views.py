from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from django.contrib.auth.views import LoginView, LogoutView
from .form import SignUpForm,LoginForm,SongForm
from .models import User,Song
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import Group, Permission

class Home(TemplateView):
    """ Home page view """
    template_name = "home.html"


class Login(LoginView):
    """ Login page view"""
    form_class = LoginForm
    template_name ='login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class Logout(LogoutView):
    """logout class"""
    pass

class SingUp(CreateView):
    """ SignUp page view """
    model = User
    template_name = 'sing_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST or None)
        if user_form.is_valid():
            user = user_form.save()
            user.save()
            user_role = user.role
            group = Group.objects.get(name=user_role)
            user.groups.add(group.id)
        return super().post(request, *args, **kwargs)

class SongCreate(CreateView):
    template_name = 'create_song.html'
    form_class = SongForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        super(SongCreate,self).post(request, *args, **kwargs)
        messages.success(request,"successfully create song.")
        return JsonResponse({"messages":"success","redirect":self.success_url})

class SongList(ListView):
    model = Song
    template_name = "song_list.html"