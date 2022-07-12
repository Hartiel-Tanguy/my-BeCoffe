from tkinter.tix import Form
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import users


class creerUtilisateur(UserCreationForm):
    class Meta:
        model = users
        fields = ['username', 'last_name', 'first_name', 'email', 'chef']