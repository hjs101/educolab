from rest_framework import serializers
<<<<<<< HEAD
from . import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
<<<<<<< HEAD
<<<<<<< HEAD
from rest_framework_simplejwt.tokens import RefreshToken
<<<<<<< HEAD
=======

>>>>>>> 1eb4a5e (Refactor : 일요일 신행상황 저장)
=======
from rest_framework_simplejwt.tokens import RefreshToken
>>>>>>> 0938bf0 (Refactor : 로그인시 넘겨주는 데이터 변경 및 프로필 사진 추가)
=======
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer

class TeacherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['name', 'username']
>>>>>>> 3494f79 (Feat : 공지사항 등록, 목록 기능 구현)
class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

# jwt token 결과 커스텀 
<<<<<<< HEAD
<<<<<<< HEAD

class SchoolInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SchoolInfo
        fields = '__all__'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    # response 커스텀 
    default_error_messages = {
        'no_active_account': {'message':'username or password is incorrect!',
                              'success': False,
                              'status' : 401}
=======
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
=======
>>>>>>> 0938bf0 (Refactor : 로그인시 넘겨주는 데이터 변경 및 프로필 사진 추가)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    # response 커스텀 
    default_error_messages = {
        'no_active_account': {'message':'username or password is incorrect!',
<<<<<<< HEAD
                            'success': False,
                            'status' : 401}
>>>>>>> 1eb4a5e (Refactor : 일요일 신행상황 저장)
=======
                              'success': False,
                              'status' : 401}
>>>>>>> 0938bf0 (Refactor : 로그인시 넘겨주는 데이터 변경 및 프로필 사진 추가)
    }
    # 유효성 검사
    def validate(self, attrs):
        data = super().validate(attrs)
<<<<<<< HEAD
<<<<<<< HEAD
        
        refresh = self.get_token(self.user)
        
         # response에 추가하고 싶은 key값들 추가
        data['name'] = self.user.name
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['userflag'] = self.user.userflag
        data['email'] = self.user.email
        data['profil'] = self.user.profil
<<<<<<< HEAD
=======

        refresh = self.get_token(self.user)

        # response에 추가할 key값
        data['username'] = self.user.username
        data['userFlag'] = self.user.userFlag
        print(data)
>>>>>>> 1eb4a5e (Refactor : 일요일 신행상황 저장)
=======
        
        refresh = self.get_token(self.user)
        
         # response에 추가하고 싶은 key값들 추가
        data['name'] = self.user.name
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['userflag'] = self.user.userflag
        data['email'] = self.user.email
<<<<<<< HEAD
        data['img'] = self.user.profil
>>>>>>> 0938bf0 (Refactor : 로그인시 넘겨주는 데이터 변경 및 프로필 사진 추가)
=======
        data['profil'] = self.user.profil
>>>>>>> 9c14433 (Refactor : 로그인 마무리)
=======
        data['schoolcode']=self.user.school.code
>>>>>>> ff62902 (Feat : 학교 정보 추가로 인한 로그인 시 반환 값 변동)
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
=======
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    userflag =serializers.BooleanField()
    name = serializers.CharField()
    birthday = serializers.DateField()
    school = serializers.CharField()
    phone_number = serializers.CharField()
    grade = serializers.IntegerField(required=False)
    class_field = serializers.IntegerField(required=False)
    subject = serializers.CharField(required=False)
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['userflag'] = self.validated_data.get('userflag','')
        data['name'] = self.validated_data.get('name','')
        data['birthday'] = self.validated_data.get('birthday','')
        data['school'] = self.validated_data.get('school','')
        data['phone_number'] = self.validated_data.get('phone_number','')
        data['grade'] = self.validated_data.get('grade','')
        data['class_field'] = self.validated_data.get('class_field','')
        data['subject'] = self.validated_data.get('subject','')
        return data
>>>>>>> 9206ccc (feat : 회원가입 기능 구현(어느정도))
