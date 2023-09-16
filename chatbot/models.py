from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=10)
    profile_pic = models.ImageField(default="profile.jpg",null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class BotUser(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=20,null=True)
    prompt = models.TextField(null=True)      
    response = models.TextField(null=True)
    prompt_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name


class FeedBack(models.Model):
    genders = (('Homo Sapiens','Homo Sapiens'),
    ('Women','Women'), ('Male','Male'), ('Female','Female'), ('Others','Others'))
    feed = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=15,choices=genders,default='Homo Sapiens')
    phone = models.CharField(max_length=10)
    location = models.CharField(max_length=50)
    descprition = models.TextField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
