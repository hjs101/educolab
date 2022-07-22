from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

<<<<<<< HEAD
    teacher_id = models.CharField(primary_key=True, max_length=45)
    name = models.CharField(max_length=30)
    birthday = models.IntegerField()
    school = models.CharField(max_length=45)
    subject = models.CharField(max_length=45)
    homeroom_teacher_flag = models.IntegerField()
    homeroom_teacher_grade = models.IntegerField(blank=True, null=True)
    homeroom_teacher_class = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=45)
<<<<<<< HEAD
    phone_number = models.IntegerField()
    email = models.CharField(max_length=45)

=======
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=45)
>>>>>>> 8af065c (Refactor : 로그인 기능 수정)
class StudentInfo(models.Model):
    student_id = models.CharField(primary_key=True, max_length=45)
    name = models.CharField(max_length=30)
    birthday = models.IntegerField()
    school = models.CharField(max_length=45)
    grade = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved 
    student_number = models.IntegerField()
    password = models.CharField(max_length=45)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=45)
    plus_point = models.IntegerField()
    minus_point = models.IntegerField()
=======
class UserInfo(AbstractUser):
    userflag = models.BooleanField(default=False)
    name = models.CharField(max_length=30,default=None)
    birthday = models.DateField(default=None)
    school = models.CharField(max_length=30,default=None)
    phone_number = models.CharField(max_length=11,default=None)
    grade = models.IntegerField(blank=True, null=True)
    class_field = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=20,null=True)
    homeroom_teacher_flag = models.IntegerField(null=True)
    plus_point = models.IntegerField(null=True)
    minus_point = models.IntegerField(null=True)
>>>>>>> e121457 (Refactor : DB수정 후 로그인 변경사항)
