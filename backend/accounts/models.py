from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserInfo(AbstractUser):
    username = models.CharField(primary_key=True,max_length=20)
    userflag = models.BooleanField(default=False)
    name = models.CharField(max_length=30,default=None)
    birthday = models.DateField(default=None)
    school = models.CharField(max_length=30,default=None)
    school_url = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11,default=None)
    grade = models.IntegerField(blank=True, null=True)
    class_field = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=20,null=True,blank=True)
    homeroom_teacher_flag = models.IntegerField(null=True)
    plus_point = models.IntegerField(default=0)
    minus_point = models.IntegerField(default=0)
    profil = models.CharField(max_length=45,null=True,blank=True)