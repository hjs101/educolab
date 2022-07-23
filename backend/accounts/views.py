from base64 import encode
from tkinter.messagebox import NO
from django.urls import is_valid_path
import jwt, datetime, json

from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import UserInfo
from django.contrib.auth.hashers import check_password

# Create your views here.
class LoginView(APIView):
    def post(self, request):


        id = request.data['id']
        password = request.data['password']
        if id is None:
            raise AuthenticationFailed('아이디를 입력하세요')

        if password is None:
            raise AuthenticationFailed('패스워드를 입력하세요')        # 학생, 교사 구분해서 객체 생성
        
        user = UserInfo.objects.filter(username=id).first()

        print(123)
        print(user)
        # print(serialize_user.data)
        #Invelid Check
        if user is None:
            raise AuthenticationFailed('아이디 또는 비밀번호가 다릅니다.')
        if check_password(password):
            raise AuthenticationFailed('아이디 또는 비밀번호가 다릅니다.')
        payload = {
            'id' : user.username,
            'exp' : (datetime.datetime.now() + datetime.timedelta(minutes=60)).strftime("%m-%d-%YT%H:%M:%S"),
            'lat' : datetime.datetime.now().strftime("%m-%d-%YT%H:%M:%S")
        }
        token = jwt.encode(payload,"EDU_COLAB_SECRET_KEY",algorithm="HS256")
        res = Response()
        # res.set_cookie(key='jwt',value=token,httponly=True)
        res.data={
            'jwt' : token,
            'userflag' : user.userFlag
        }
        return res