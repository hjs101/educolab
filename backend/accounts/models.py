<<<<<<< HEAD
from asyncio.windows_events import NULL
from django.contrib.auth.models import AbstractUser
from django.db import models

from pointshop.models import PTitle, Icon

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
=======
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

>>>>>>> 1d03a62 (Backend file 삽입)
class SchoolInfo(models.Model):
    code = models.CharField(max_length=7,primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

<<<<<<< HEAD
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
=======
class UserInfo(AbstractUser):
    username = models.CharField(primary_key=True,max_length=20)
>>>>>>> 1d03a62 (Backend file 삽입)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e82d912 (Repactor : 로그인 기능  simple jwt 변경사항)
=======
    profil = models.CharField(max_length=45,null=True,blank=True)
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
    acc_point = models.IntegerField(default=0)
<<<<<<< HEAD
>>>>>>> 40812b7 (Feat : Mypage 생성)
=======
=======
=======
    profil = models.ImageField(blank=True, upload_to='accounts/profils')
>>>>>>> 707b7a2 (Feat : 프로필 사진 변경)
=======
    profil = models.ImageField(blank=True, upload_to='accounts/profils' ,default='accounts/profils/test01.jpg')
>>>>>>> 2b5572c (Feat : 프로필 사진 변경 구현)
    acc_point = models.IntegerField(default=0, null=True)
<<<<<<< HEAD
>>>>>>> 59ac581 (Feat : Mypage 기능 구현)
=======
    wear_title = models.ForeignKey(PTitle,null=True,on_delete=models.SET_NULL)
    own_title = models.ManyToManyField(PTitle,related_name='title_owner')
    own_icon = models.ManyToManyField(Icon, related_name='icon_owner')

>>>>>>> 4910d64 (feat : 상점 기능 구현, 마이페이지 칭호 변경 구현)
    
class PointLog(models.Model):
    teacher = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, related_name="point_teacher")
    student = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="point_student")
    content = models.CharField(max_length=45)
    point = models.IntegerField()
<<<<<<< HEAD
>>>>>>> b9da983 (Feat : mypage 구현중)
=======
    created_at = models.DateField(auto_now=True)
>>>>>>> 59ac581 (Feat : Mypage 기능 구현)
=======
    profil = models.CharField(max_length=45,null=True,blank=True)
>>>>>>> 1d03a62 (Backend file 삽입)
