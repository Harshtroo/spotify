from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# from django.contrib.auth.models import User
from .models import User,Song

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = User
        fields = ["username","password"]


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ["username","email","mobile_number","role","password1","password2"]

    def clean_description(self):
        if not self.cleaned_data['description'].strip():
            raise forms.ValidationError('Your error message here')


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["name","singer_name","category"]

    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def soft_delete(self):
        '''soft delete funcction'''
        self.is_deleted= True
        self.save()


class SongEditForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["name","singer_name","category"]
