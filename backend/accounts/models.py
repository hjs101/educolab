from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class SchoolInfo(models.Model):
    code = models.CharField(max_length=7,primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class UserInfo(AbstractUser):
    username = models.CharField(primary_key=True,max_length=20)
    userflag = models.BooleanField(default=False, blank=True)
    name = models.CharField(max_length=30,default=None,blank=True)
    birthday = models.DateField(default=None,blank=True)
    school = models.ForeignKey(SchoolInfo,on_delete=models.CASCADE,db_column='school', related_name='school_student')
    phone_number = models.CharField(max_length=11,blank=True)
    grade = models.IntegerField(blank=True,null=True)
    class_field = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=20,null=True,blank=True)
    homeroom_teacher_flag = models.IntegerField(null=True)
    plus_point = models.IntegerField(default=0)
    minus_point = models.IntegerField(default=0)
    profil = models.ImageField(blank=True, upload_to='accounts/profils' ,default='accounts/profils/test01.jpg')
    acc_point = models.IntegerField(default=0, null=True)
    
class PointLog(models.Model):
    teacher = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, related_name="point_teacher")
    student = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="point_student")
    content = models.CharField(max_length=45)
    point = models.IntegerField()
    created_at = models.DateField(auto_now=True)