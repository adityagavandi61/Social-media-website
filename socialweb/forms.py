# forms.py

from django import forms
from .models import UserRegister,ViewerRegister

class UserRegisterForm(forms.Form):
    class user:
        model1 = UserRegister
        fields = ['name', 'gmail', 'address', 'page_name', 'phone_number', 'password']

class ViewerRegisterForm(forms.Form):
    class viewer:
        model2 = ViewerRegister
        fields = ['name', 'gmail','password']

