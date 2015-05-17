from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from datetime import datetime 




class Userlog(models.Model):
    
    #author = models.ForeignKey(User)
    usernameLog =  models.CharField(max_length=10)
    passwordLog =  models.CharField(max_length=10)
        #self.save()

    def __unicode__(self):
        return self.usernameLog
        
        



# Create your models here.
class Post(models.Model):
    
    festival_name = models.CharField(max_length=200)
    #set_date = models.DateField(default=timezone.now())
    set_date = models.DateField()
    created_date = models.DateTimeField(default=datetime.now)
    published_date = models.DateTimeField(blank=True, null=True)
    festival_story = models.TextField(default=None)
    
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', default=None)

    def publish(self):
        self.published_date = timezone.now() 
        #self.save()

    def __unicode__(self):
        return self.festival_name
        

