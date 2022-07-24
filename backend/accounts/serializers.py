from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer

""" User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = '__all__' """

class CustomRegisterSerializer(RegisterSerializer):
    userflag =serializers.BooleanField()
    name = serializers.CharField()
    birthday = serializers.DateField()
    school = serializers.CharField()
    phone_number = serializers.CharField()
    grade = serializers.IntegerField()
    class_field = serializers.IntegerField()
    subject = serializers.CharField()
    homeroom_teacher_flag = serializers.IntegerField()
    plus_point = serializers.IntegerField()
    minus_point = serializers.IntegerField()

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
        data['homeroom_teacher_flag'] = self.validated_data.get('homeroom_teacher_flag','')
        data['plus_point'] = self.validated_data.get('plus_point','')
        data['minus_point'] = self.validated_data.get('minus_point','')
        return data