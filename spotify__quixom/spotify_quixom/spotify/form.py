from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User,Song,PlayList

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username","password"]

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        for field in self.fields:
            self.fields[field].required = True

class SignUpForm(UserCreationForm):


    class Meta:
        model = User
        fields = ["username","email","mobile_number","role","password1","password2"]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        for field in self.fields:
            self.fields[field].required = True

    def clean_description(self):
        if not self.cleaned_data['description'].strip():
            raise forms.ValidationError('username already exists.')


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["name","singer_name","category"]

    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        for field in self.fields:
            self.fields[field].required = True

    def soft_delete(self):
        '''soft delete funcction'''
        self.is_deleted= True
        self.save()


class SongEditForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["name","singer_name","category"]


class CreatePlayListForm(forms.ModelForm):
    class Meta:
        model = PlayList
        fields = ["list_name","songs"]

    def __init__(self, *args, **kwargs):
        super(CreatePlayListForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        for field in self.fields:
            self.fields[field].required = True