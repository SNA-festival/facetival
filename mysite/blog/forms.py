# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _

from .models import Post
from .models import Userlog
from django.contrib.auth.models import User
from datetime import date


class UserForm(ModelForm):
    username = forms.CharField(label='帳號')
    password = forms.CharField(widget=forms.PasswordInput,label='密碼')
    email = forms.CharField(label='信箱')
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        widgets = {
            'password': forms.PasswordInput(),
        }

class UserlogForm(forms.ModelForm):
    
    usernameLog = forms.CharField(label='帳號')
    passwordLog = forms.CharField(widget=forms.PasswordInput,label='密碼')
    class Meta:
        model = Userlog
        fields = ('usernameLog','passwordLog')
        
        widgets = {
            'passwordLog': forms.PasswordInput(),
        }
        
        

class PostForm(forms.ModelForm):

    docfile = forms.FileField(label='')
    set_date = forms.DateField(label='節慶日期', initial=date.today())
    festival_name = forms.CharField(label='節慶名稱')
    festival_story= forms.CharField(label='節慶故事',widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ('docfile','festival_name','set_date','festival_story')


        


