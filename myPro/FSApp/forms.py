# import imp
# from ipaddress import ip_address
# from socket import fromshare
# from django import forms
# from django.contrib.auth.models import User
# from app1_lvl5.models import UserProfileInfo
# from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from FSApp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
