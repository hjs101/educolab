from sre_constants import SUCCESS
from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from .serializers import SchoolInfoSerializer
from .models import SchoolInfo, UserInfo
from .helper import email_auth_num
from my_settings import EMAIL_HOST_USER

# Create your views here.

class SchoolInfoView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        search = request.data['schoolname']
        school = SchoolInfo.objects.filter(name__contains=search)
        serializer = SchoolInfoSerializer(school,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class CheckUsernameView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        username = request.data.get('username')

        try:
            checkname = UserInfo.objects.get(username=username)
        except:
            checkname = None

        if checkname is None:
            dup = "success"
        else:
            dup = "fail"
        context = {"dup": dup}
        return Response(context)

class SendSignupEmailView(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        email = request.data['email']
        auth_num = email_auth_num()
        print(auth_num)
        print(email)
        send_mail(subject='educolab 회원가입 이메일 인증 메일입니다',message=auth_num,recipient_list=[email],from_email=EMAIL_HOST_USER)
        return Response({'auth_num': auth_num})

class FindIDView(APIView):
    pass
