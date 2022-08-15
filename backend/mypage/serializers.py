from rest_framework import serializers
<<<<<<< HEAD

from pointshop.serializers import TitleSerializer
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
from . import models
from accounts.models import PointLog
from django.contrib.auth import get_user_model
from accounts.serializers import UserNameSerializer

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
        fields = ['username','email','userflag','name','birthday','phone_number','subject','homeroom_teacher_flag','grade','class_field','profil']
        
class StudentSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    wear_title = TitleSerializer(read_only=True)
    own_title = TitleSerializer(read_only=True,many=True)

    class Meta:
        model = get_user_model()
        fields = ['username','email','userflag','name','birthday','phone_number','grade','class_field','profil','plus_point','minus_point','acc_point','wear_title','own_title',]

class TeacherUpdateSerializer(serializers.ModelSerializer):
    profil = ProfilSerializer(read_only=True)
    class Meta:
        model = get_user_model()
        fields = ['username','email','userflag','name','birthday','phone_number','subject','homeroom_teacher_flag','grade','class_field','profil']
        
class StudentUpdateSerializer(serializers.ModelSerializer):
    wear_title = TitleSerializer(read_only=True)
    own_title = TitleSerializer(read_only=True,many=True)
    profil = ProfilSerializer(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username','email','userflag','name','birthday','phone_number','grade','class_field','profil','plus_point','minus_point','acc_point','wear_title','own_title',]
=======
    class Meta:
        model = get_user_model()
        fields = ['username','email','userflag','name','birthday','phone_number','grade','class_field','profil','plus_point','minus_point','acc_point']
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
        

class SearchStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username','name','grade','class_field']
