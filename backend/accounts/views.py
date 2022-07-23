<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
from re import L
>>>>>>> 9a0c0d9 (feat : 학교이름 검색 기능 구현 - 홍찬기)
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SchoolInfoSerializer
from .models import SchoolInfo

# Create your views here.
<<<<<<< HEAD
=======
from base64 import encode
from tkinter.messagebox import NO
from django.urls import is_valid_path
import jwt, datetime, json

=======
>>>>>>> 51dde47 (Refactor : requirements.txt 파일 수정 및 url, views 수정사항 적용)
from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
class LoginView(APIView):
    def post(self, request):
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e82d912 (Repactor : 로그인 기능  simple jwt 변경사항)


        id = request.data['id']
        password = request.data['password']
        if id is None:
            raise AuthenticationFailed('아이디를 입력하세요')

        if password is None:
            raise AuthenticationFailed('패스워드를 입력하세요')        # 학생, 교사 구분해서 객체 생성
<<<<<<< HEAD
<<<<<<< HEAD
        if userFlag == "teacher":
            return teacherLogin()
        else:
            return studentLogin()
>>>>>>> 8af065c (Refactor : 로그인 기능 수정)
=======
        
=======

>>>>>>> e82d912 (Repactor : 로그인 기능  simple jwt 변경사항)
        user = UserInfo.objects.filter(username=id).first()

        print(123)
        print(user)
        # print(serialize_user.data)
        #Invelid Check
        if user is None:
            raise AuthenticationFailed('아이디 또는 비밀번호가 다릅니다.')
<<<<<<< HEAD
        if check_password(password):
=======
        if check_password(password, user.password):
>>>>>>> e82d912 (Repactor : 로그인 기능  simple jwt 변경사항)
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
<<<<<<< HEAD
        return res
>>>>>>> e121457 (Refactor : DB수정 후 로그인 변경사항)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 9e2d7fd (Style : UserInfo DB 등록)
=======
>>>>>>> 6f9cfef (style : 모델 변경)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 2babd3d (Merge branch 'back' of https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102 into back)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 7b2ad8a (Test : nyam)
=======
        user = authenticate(
            login_id=request.data.get("id"), password=request.data.get("password")
        )
        if user is not None:
            serializer = UserinfoSerializer(user)
            token = MyTokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 1eb4a5e (Refactor : 일요일 신행상황 저장)
=======
        return res
>>>>>>> e82d912 (Repactor : 로그인 기능  simple jwt 변경사항)
=======
>>>>>>> 51dde47 (Refactor : requirements.txt 파일 수정 및 url, views 수정사항 적용)
=======
from rest_framework.decorators import APIView
""" from .serializers import SignupSerializer """
from rest_framework.response import Response

""" class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201) """
>>>>>>> 9206ccc (feat : 회원가입 기능 구현(어느정도))
=======

class SchoolInfoView(APIView):
    
    def get(self, request):
        search = request.data['schoolname']
        school = SchoolInfo.objects.filter(name__contains=search)
        serializer = SchoolInfoSerializer(school,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
>>>>>>> 9a0c0d9 (feat : 학교이름 검색 기능 구현 - 홍찬기)
