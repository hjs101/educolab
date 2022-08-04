from rest_framework import serializers
from . import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer


# jwt token 결과 커스텀 

class SchoolInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SchoolInfo
        fields = '__all__'

