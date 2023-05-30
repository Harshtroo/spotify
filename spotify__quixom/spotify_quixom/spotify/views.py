from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .form import SignUpForm,LoginForm
from .models import User
from django.urls import reverse_lazy
from django.contrib import messages

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
    template_name = 'sing_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    