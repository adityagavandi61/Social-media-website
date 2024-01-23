# forms.py

from django import forms
from .models import UserRegister,ViewerRegister

class UserRegisterForm(forms.Form):
    class user:
        model = UserRegister
        fields = ['name', 'gmail', 'address', 'page_name', 'phone_number', 'password','date']

class ViewerRegisterForm(forms.Form):
    class viewer:
        model = ViewerRegister
        fields = ['name', 'gmail','password','date']

