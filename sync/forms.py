from django import forms
from django.contrib.auth.forms import AuthenticationForm

class loginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    pass