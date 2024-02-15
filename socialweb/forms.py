# forms.py

# from django import forms
# from django.contrib.auth.models import User,auth
# # from .models import UserRegister,ViewerRegister


# class User(forms.Form):
#     class user:
#         model = User
#         fields = ['name', 'gmail', 'address', 'page_name', 'phone_number', 'password','date']


# class ViewerRegisterForm(forms.Form):
#     class viewer:
#         model = ViewerRegister
#         fields = ['name', 'gmail','password','date']

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
	class Meta:
		model = Snippet
		fields = ['blogname',
				'img',
				'blogauth',
				'blogdes'
				]
