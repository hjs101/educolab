from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 9e2d7fd (Style : UserInfo DB 등록)
=======
=======
>>>>>>> 559df98 ( Feat : 버그 수정)
class SchoolInfo(models.Model):
    code = models.CharField(max_length=7,primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

<<<<<<< HEAD
>>>>>>> 02ef900 (feat : 회원가입기능 학교모델 추가)
class UserInfo(AbstractUser):
    username = models.CharField(primary_key=True,max_length=20)
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
    plus_point = models.IntegerField(null=True)
<<<<<<< HEAD
    minus_point = models.IntegerField(null=True)
>>>>>>> e121457 (Refactor : DB수정 후 로그인 변경사항)
=======
    minus_point = models.IntegerField(null=True)
>>>>>>> 9e2d7fd (Style : UserInfo DB 등록)
=======
    plus_point = models.IntegerField(default=0)
    minus_point = models.IntegerField(default=0)
    profil = models.CharField(max_length=45,null=True,blank=True)
>>>>>>> 2babd3d (Merge branch 'back' of https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102 into back)
=======
=======
class UserInfo(AbstractUser):
    username = models.CharField(primary_key=True,max_length=20)
>>>>>>> 559df98 ( Feat : 버그 수정)
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e82d912 (Repactor : 로그인 기능  simple jwt 변경사항)
=======
    profil = models.CharField(max_length=45,null=True,blank=True)
>>>>>>> 0938bf0 (Refactor : 로그인시 넘겨주는 데이터 변경 및 프로필 사진 추가)
=======
    userflag = models.BooleanField(default=False, blank=True)
    name = models.CharField(max_length=30,default=None,blank=True)
    birthday = models.DateField(default=None,blank=True)
    school = models.CharField(max_length=30,blank=True)
    phone_number = models.CharField(max_length=11,blank=True)
    grade = models.IntegerField(blank=True)
    class_field = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=20,null=True,blank=True)
    homeroom_teacher_flag = models.IntegerField(null=True)
    plus_point = models.IntegerField(default=0)
    minus_point = models.IntegerField(default=0)
>>>>>>> 9206ccc (feat : 회원가입 기능 구현(어느정도))
=======
    profil = models.CharField(max_length=45,null=True,blank=True)
>>>>>>> 559df98 ( Feat : 버그 수정)
