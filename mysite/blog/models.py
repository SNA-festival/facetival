from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea

class Userlog(models.Model):
    
    #author = models.ForeignKey(User)
    author =  models.CharField(max_length=10)
    password =  models.CharField(max_length=10)
        #self.save()

    def __unicode__(self):
        return self.author


# Create your models here.
class Post(models.Model):
    
    festival_name = models.CharField(max_length=200)
    set_date = models.DateField(default=timezone.now())
    
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
    festival_story = models.TextField(default=None)
    
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', default=None)

    def publish(self):
        self.published_date = timezone.now() 
        #self.save()

    def __unicode__(self):
        return self.festival_name
        

