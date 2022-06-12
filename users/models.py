from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): 
    bio = models.TextField(max_length=200,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
   

    

 