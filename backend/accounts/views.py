<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
from sre_constants import SUCCESS
>>>>>>> 25d0df5 (feat: 회원가입에서 이메일 인증메일 보내기 기능 구현 , id 중복체크 기능 완성 - 홍찬기)
=======
from sre_constants import SUCCESS
>>>>>>> d0de156 ( Fix : get 방식으로 적용 중)
=======
>>>>>>> ea51fa4 (feat : 과제기능 생성,삭제 구현, 나머지는 더 구현해야함)
=======
>>>>>>> 1d03a62 (Backend file 삽입)
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
<<<<<<< HEAD
<<<<<<< HEAD
from educolab.settings import EMAIL_HOST_USER
=======
>>>>>>> b9da983 (Feat : mypage 구현중)

# Create your views here.
<<<<<<< HEAD
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
=======
>>>>>>> d0de156 ( Fix : get 방식으로 적용 중)
=======
from educolab.settings import EMAIL_HOST_USER

# Create your views here.
>>>>>>> 1d03a62 (Backend file 삽입)

class SchoolInfoView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        search = request.GET.get('schoolname')
=======
        search = request.GET['schoolname']
>>>>>>> 0970789 (Style : back 브랜치 테스트)
=======
        search = request.GET.get('schoolname')
>>>>>>> 5e7e020 (feat : get 정보 방식 수정)
=======
        search = request.GET.get('schoolname')
>>>>>>> 8256ee0 (feat : get, post 입력방식 변화)
        school = SchoolInfo.objects.filter(name__contains=search)
        serializer = SchoolInfoSerializer(school,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9a0c0d9 (feat : 학교이름 검색 기능 구현 - 홍찬기)
=======
=======
>>>>>>> d0de156 ( Fix : get 방식으로 적용 중)
=======
        search = request.GET.get('schoolname')
        school = SchoolInfo.objects.filter(name__contains=search)
        serializer = SchoolInfoSerializer(school,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
>>>>>>> 1d03a62 (Backend file 삽입)

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        email = request.data.get('email')
=======
        email = request.POST.get('email')
>>>>>>> 8256ee0 (feat : get, post 입력방식 변화)
=======
        email = request.POST.get('email')
>>>>>>> 559df98 ( Feat : 버그 수정)
=======
        email = request.data.get('email')
>>>>>>> 80321b2 (Fix : 버그수정)
=======
        email = request.data.get('email')
>>>>>>> d73082d (feat : back branch 수정)
=======
        email = request.data.get('email')
>>>>>>> 1d03a62 (Backend file 삽입)
        auth_num = email_auth_num()
        print(email)
        send_mail(subject='educolab 회원가입 이메일 인증 메일입니다',message=auth_num,recipient_list=[email],from_email=EMAIL_HOST_USER)
        context = {
            'auth_num' : auth_num,
        }
        return Response(context)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
class FindIDView(APIView):
    pass
<<<<<<< HEAD
>>>>>>> 668c397 (feat : 회원가입정보 subject,userflag 수정)
=======
>>>>>>> 25d0df5 (feat: 회원가입에서 이메일 인증메일 보내기 기능 구현 , id 중복체크 기능 완성 - 홍찬기)
=======
=======
>>>>>>> 1d03a62 (Backend file 삽입)
class FindUsernameView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        name = request.POST.get('name')
        email = request.POST.get('email')
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 966ca14 (feat: 회원기능에서 POST 입력방식 변경)
=======
>>>>>>> 45cae29 ( Fix : 프론트 merge 전 커밋)
=======
class FindUsernameView(APIView):
    permission_classes = (AllowAny,)

<<<<<<< HEAD
    def get(self, request):
        name = request.GET.get('name')
        email = request.GET.get('email')
>>>>>>> d0de156 ( Fix : get 방식으로 적용 중)
=======
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
>>>>>>> 5e7e020 (feat : get 정보 방식 수정)
=======
>>>>>>> 8256ee0 (feat : get, post 입력방식 변화)
=======
        name = request.data.get('name')
        email = request.data.get('email')
>>>>>>> 23fc5b1 (Fix : 충돌 수정)
=======
        name = request.POST.get('name')
        email = request.POST.get('email')
>>>>>>> 559df98 ( Feat : 버그 수정)
=======
        name = request.data.get('name')
        email = request.data.get('email')
>>>>>>> 80321b2 (Fix : 버그수정)
=======
        name = request.data.get('name')
        email = request.data.get('email')
>>>>>>> d73082d (feat : back branch 수정)
=======
        name = request.data.get('name')
        email = request.data.get('email')
>>>>>>> 1d03a62 (Backend file 삽입)

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        username = request.POST.get('username','')
=======
=======
        print(request.data)
>>>>>>> f86710a (Feat : 비밀번호 변경 구현 완료)
        name = request.data.get('name')
        email = request.data.get('email')
        username = request.data.get('username')
<<<<<<< HEAD
>>>>>>> d0de156 ( Fix : get 방식으로 적용 중)
=======
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
>>>>>>> 8256ee0 (feat : get, post 입력방식 변화)
=======
        name = request.data.get('name')
        email = request.data.get('email')
        username = request.data.get('username')
>>>>>>> 80321b2 (Fix : 버그수정)
=======
        name = request.data.get('name')
        email = request.data.get('email')
        username = request.data.get('username')
>>>>>>> d73082d (feat : back branch 수정)
=======
        name = request.data.get('name')
        email = request.data.get('email')
        username = request.data.get('username')
>>>>>>> d2fc3f3 (feat : 비밀번호 초기화 및 변경 기능 구현)
        
=======
>>>>>>> fa227ef (Feat & Fix : 과제 생성/수정 기능 완료, 나머지 기능 진행 중, 회원 관리 부분 컴포넌트화 및 버그 수정 중)
=======
        name = request.data.get('name')
        email = request.data.get('email')
        username = request.data.get('username')
        
>>>>>>> 1d03a62 (Backend file 삽입)
        try:
            userinfo = UserInfo.objects.get(name=name,username=username)
        except:
            userinfo = None
<<<<<<< HEAD
=======
        
>>>>>>> 1d03a62 (Backend file 삽입)
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

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0c829cf (feat: 아이디 찾기 기능 구현)
=======
>>>>>>> d0de156 ( Fix : get 방식으로 적용 중)
=======
=======
>>>>>>> 4eef746 (feat : homework 에도 비밀번호 변경기능 올려놓음)
=======
>>>>>>> 1d03a62 (Backend file 삽입)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return Response(context)
>>>>>>> d2fc3f3 (feat : 비밀번호 초기화 및 변경 기능 구현)
=======
        return Response(context)
>>>>>>> 4eef746 (feat : homework 에도 비밀번호 변경기능 올려놓음)
=======
        return Response(context)
>>>>>>> 1d03a62 (Backend file 삽입)
=======
        return Response(context)

class CheckPasswordView(APIView):

    def post(self, request):
        input_password = request.data.get('password')
        check = check_password(input_password,request.user.password)
        return Response({"success" : check})
<<<<<<< HEAD
>>>>>>> 5ee470c (feat : pw 확인 기능 구현)
=======

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
                print(data)
                response.data = {"success" : True, "message" : "Login 성공","access" : data['access'],"userinfo" : userinfo}
                return response
        else:
            return Response({"success" : False, "message": "올바른 번호를 입력하세요"}, status=status.HTTP_404_NOT_FOUND)
>>>>>>> 4f92e2a (fix : 다양한 기능 수정)
