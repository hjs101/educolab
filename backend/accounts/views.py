from base64 import encode
from tkinter.messagebox import NO
from django.urls import is_valid_path
import jwt, datetime

from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import TeacherSerializer, StudentSerializer
from .models import TeacherInfo, StudentInfo


# Create your views here.
class LoginView(APIView):
    def post(self, request):
        teacher = TeacherInfo("3","홍길동",'1997-05-28',"싸피중학교","국어",0,None,None,"123123123","01012341234","qweasd@naver.com")
        serial = TeacherSerializer(data=teacher)
        teacher.save()
        print(teacher.__str__)
        print(serial)
        if serial.is_valid(raise_exception=True):
            serial.save()
        def studentLogin():
            user = StudentInfo.objects.filter(student_id=id)
            serialize_user = StudentSerializer(user)

            # JSON 변환
            json_user = JSONRenderer().render(serialize_user.data);

            #Invelid Check
            if user is None:
                raise AuthenticationFailed('아이디 또는 비밀번호가 다릅니다.')

            if not user.check_password(password):
                raise AuthenticationFailed('아이디 또는 비밀번호가 다릅니다.')
            payload = {
                'id' : user.student_id,
                'exp' : datetime.datetime.now() + datetime.timedelta(minutes=60),
                'lat' : datetime.datetime.now()
            }
            
            token = jwt.encode(payload,"MY_SECRET_KEY",algorithm="HS256")
            
            res = Response()
            res.set_cookie(key='jwt',value=token,httponly=True)
            res.data={
                'jwt' : token
            }
            return res
        
        def teacherLogin():
            user = TeacherInfo.objects.filter(teacher_id=id).first()
            serialize_user = TeacherSerializer(user)

            # JSON 변환
            json_user = JSONRenderer().render(serialize_user.data);
            print(123)
            print(user)
            print(serialize_user)
            #Invelid Check
            if user is None:
                raise AuthenticationFailed('아이디 또는 비밀번호가 다릅니다.')

            if not user.check_password(password):
                raise AuthenticationFailed('아이디 또는 비밀번호가 다릅니다.')
            payload = {
                'id' : user.teacher_id,
                'userflag' : userFlag,
                'exp' : datetime.datetime.now() + datetime.timedelta(minutes=60),
                'lat' : datetime.datetime.now()
            }
            
            token = jwt.encode(payload,"MY_SECRET_KEY",algorithm="HS256")
            
            res = Response()
            res.set_cookie(key='jwt',value=token,httponly=True)
            res.data={
                'jwt' : token
            }
            return res
        
        id = request.data['id']
        password = request.data['password']
        userFlag = request.data['userFlag']
        # 학생, 교사 구분해서 객체 생성
        if userFlag == "teacher":
            return teacherLogin()
        else:
            return studentLogin()
