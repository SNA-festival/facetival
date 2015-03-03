# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _

from .models import Post
from .models import Userlog
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserlogForm(forms.ModelForm):
    
    UserName = forms.CharField(label='帳號')
    password = forms.CharField(widget=forms.PasswordInput,label='密碼')
    class Meta:
        model = Userlog
        fields = ('UserName','password')
        
        widgets = {
            'password': forms.PasswordInput(),
        }
        
        

class PostForm(forms.ModelForm):

    docfile = forms.FileField(label='')
    set_date = forms.DateField(label='節慶日期')
    festival_name = forms.CharField(label='節慶名稱')
    festival_story= forms.CharField(label='節慶故事',widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ('docfile','festival_name','set_date','festival_story')


        


