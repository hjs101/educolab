from rest_framework import serializers
from . import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['name', 'username']

class HomeworkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('name','username')

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
        data['profil'] = self.user.profil
        data['schoolcode']=self.user.school.code
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

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
