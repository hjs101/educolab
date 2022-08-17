from rest_framework import serializers
<<<<<<< HEAD

<<<<<<< HEAD
from pointshop.serializers import TitleSerializer
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
from pointshop.serializers import TitleSerializer, IconSerializer
>>>>>>> e17f31c (Feat : 마이 페이지 칭호, 배지 적용 부분 진행 중)
from . import models
from accounts.models import PointLog
from django.contrib.auth import get_user_model
from accounts.serializers import UserNameSerializer, SchoolInfoSerializer

# jwt token 결과 커스텀 

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['profil']

class PointlogSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    student = UserNameSerializer(read_only=True)
    class Meta:
        model = PointLog
        fields = '__all__'
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username','email','userflag','name','birthday','phone_number','subject','homeroom_teacher_flag','grade','class_field', 'profil']
        
class StudentSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    wear_title = TitleSerializer(read_only=True)
    own_title = TitleSerializer(read_only=True,many=True)

    class Meta:
        model = get_user_model()
<<<<<<< HEAD
        fields = ['username','email','userflag','name','birthday','phone_number','grade','class_field','profil','plus_point','minus_point','acc_point','wear_title','own_title','wear_icon','own_icon',]
=======
        fields = ['username','email','userflag','name','birthday','phone_number','grade','class_field','profil','plus_point','minus_point','acc_point','wear_title','own_title','wear_icon', 'own_icon']
>>>>>>> db26c2a (Style & Fix : 스타일 및 오류 수정)

class TeacherUpdateSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer(read_only=True)
    school = SchoolInfoSerializer(read_only=True)
    class Meta:
        model = get_user_model()
        fields = ['username','email','userflag','name','birthday','phone_number','subject','homeroom_teacher_flag','grade','class_field','profil','school']
        
class StudentUpdateSerializer(serializers.ModelSerializer):
    wear_title = TitleSerializer(read_only=True)
    own_title = TitleSerializer(read_only=True,many=True)
    wear_icon = IconSerializer(read_only=True)
    own_icon = IconSerializer(read_only=True,many=True)
    profil = ProfilSerializer(read_only=True)

    class Meta:
        model = get_user_model()
<<<<<<< HEAD
        fields = ['username','email','userflag','name','birthday','phone_number','grade','class_field','profil','plus_point','minus_point','acc_point','wear_title','own_title',]
=======
    class Meta:
        model = get_user_model()
        fields = ['username','email','userflag','name','birthday','phone_number','grade','class_field','profil','plus_point','minus_point','acc_point']
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
        fields = ['username','email','userflag','name','birthday','phone_number','grade','class_field','profil','plus_point','minus_point','acc_point','wear_title','own_title','wear_icon', 'own_icon']
>>>>>>> e17f31c (Feat : 마이 페이지 칭호, 배지 적용 부분 진행 중)
        

class SearchStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username','name','grade','class_field']
