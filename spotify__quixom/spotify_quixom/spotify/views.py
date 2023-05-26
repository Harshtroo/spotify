from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class Home(TemplateView):
    template_name = "home.html"
    
    
    
class Login(LoginView):
    template_name ='login.html'