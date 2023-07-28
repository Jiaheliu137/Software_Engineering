from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class ChangeUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=32, widget=forms.PasswordInput, label='Old password')
    new_password1 = forms.CharField(max_length=32, widget=forms.PasswordInput, label='New password')
    new_password2 = forms.CharField(max_length=32, widget=forms.PasswordInput, label='Confirm password')
