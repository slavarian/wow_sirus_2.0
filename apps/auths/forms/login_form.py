from django import forms
from auths.models import  MyUser
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ['email', 'password'] 