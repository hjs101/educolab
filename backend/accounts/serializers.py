from rest_framework import serializers
from . import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from educolab.settings import SECRET_KEY
import jwt

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['name', 'username']

class HomeworkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('name','username','grade','class_field',)

class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

# jwt token 결과 커스텀 

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
    }
    # 유효성 검사
    def validate(self, attrs):
        data = super().validate(attrs)
        
        refresh = self.get_token(self.user)
        
         # response에 추가하고 싶은 key값들 추가
        data['name'] = self.user.name
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['userflag'] = self.user.userflag
        data['email'] = self.user.email
        data['profil'] = self.user.profil.url
        data['schoolname']=self.user.school.name
        return data

class ProfilFileSerializer(serializers.ModelSerializer):
    profil = serializers.ImageField(use_url=True)
    class Meta:
        model = models.UserInfo
        fields = 'profil'

class MyTokenRefershSerializer(TokenRefreshSerializer):
        # response 커스텀 
    default_error_messages = {
        'no_active_account': {'message':'username or password is incorrect!',
                              'success': False,
                              'status' : 401}
    }
    # 유효성 검사
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # refresh = self.get_token(self.user)
        decode_data = jwt.decode(data['access'], SECRET_KEY, algorithms=['HS256'])
        print(decode_data)
        # response에 추가하고 싶은 key값들 추가
        user = models.UserInfo.objects.get(username=decode_data['user_id'])
        data['name'] = user.name
        data['userflag'] = user.userflag
        data['email'] = user.email
        data['profil'] = user.profil.url
        data['schoolname']=user.school.name
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class MyTokenRefershView(TokenRefreshView):
    serializer_class = MyTokenRefershSerializer

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
