from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf


from .serializers import SchoolInfoSerializer
from .models import SchoolInfo, UserInfo
from .helper import email_auth_num
from educolab.settings import EMAIL_HOST_USER

# Create your views here.

class SchoolInfoView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        search = request.GET.get('schoolname')
        school = SchoolInfo.objects.filter(name__contains=search)
        serializer = SchoolInfoSerializer(school,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class CheckUsernameView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        username = request.GET.get('username')

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
        email = request.data.get('email')
        auth_num = email_auth_num()
        send_mail(subject='educolab 회원가입 이메일 인증 메일입니다',message=auth_num,recipient_list=[email],from_email=EMAIL_HOST_USER)
        context = {
            'auth_num' : auth_num,
        }
        return Response(context)

class FindUsernameView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')

        try:
            user = UserInfo.objects.get(name=name,email=email)
        except:
            user = None
        
        if user == None:
            context = {
                'success' : False,
            }
        else:
            username = user.username
            context = {
                'success' : True,
                'username' : username,
            }
        
        return Response(context)

class SendPWEmailView(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        name = request.data.get('name')
        email = request.data.get('email')
        username = request.data.get('username')
        try:
            userinfo = UserInfo.objects.get(name=name,username=username)
        except:
            userinfo = None
        if userinfo == None:
            context = {
                "success" : False,
                "message" : "이름과 아이디가 일치하는 회원이 없습니다"
            }
            return Response(context)
        
        if email == userinfo.email:
            auth_num = email_auth_num()
            send_mail(subject='educolab 비밀번호 이메일 인증 메일입니다',message=auth_num,recipient_list=[email],from_email=EMAIL_HOST_USER)
            context = {
                "success" : True,
                "auth_num" : auth_num,
            }
            return Response(context)
        else:
            context = {
                "success" : False,
                "message" : "이메일이 일치하지 않습니다"
            }
            return Response(context)

class ChangePWView(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        name = request.data.get('name')
        email = request.data.get('email')
        username = request.data.get('username')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')

        if password1 != password2:
            context = {
                "success" : False,
                "message" : "비밀번호가 일치하지 않습니다"
            }
            return Response(context)
        if len(password1) < 8:
            context = {
                "success" : False,
                "message" : "비밀번호는 8자 이상, 영문과 숫자를 혼합해야합니다"
            }
        if password1.isalpha() or password1.isdecimal():
            context = {
                "success" : False,
                "message" : "비밀번호는 8자 이상, 영문과 숫자를 혼합해야합니다"
            }
            return Response(context)
        userinfo = UserInfo.objects.get(name=name,email=email,username=username)
        userinfo.set_password(password1)
        userinfo.save()

        context = {
            "success" : True,
            "message" : "비밀번호가 성공적으로 변경되었습니다"
        }
        return Response(context)

class CheckPasswordView(APIView):

    def post(self, request):
        input_password = request.data.get('password')
        check = check_password(input_password,request.user.password)
        return Response({"success" : check})

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

class LoginView(APIView):
    permission_classes = [ AllowAny,]

    def post(self, request):
        response = Response()
        username = request.data.get('username',None)
        password = request.data.get('password',None)
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key= settings.SIMPLE_JWT['AUTH_COOKIE'],
                    value = data['refresh'],
                    expires = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                userinfo = {
                    "name" : user.name,
                    "userflag" : user.userflag,
                    "username" : user.username,
                    "profil" : user.profil.url,
                    "schoolname" : user.school.name
                }
                csrf.get_token(request)
                response.data = {"success" : True, "message" : "Login 성공","access" : data['access'],"userinfo" : userinfo}
                return response
        else:
            return Response({"success" : False, "message": "올바른 번호를 입력하세요"}, status=status.HTTP_404_NOT_FOUND)