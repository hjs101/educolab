"""educolab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from . import views
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from .serializers import MyTokenObtainPairView
##aaadd
urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
    path('/login', views.login, name = "login"),
=======
>>>>>>> 6f9cfef (style : 모델 변경)
=======
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
<<<<<<< HEAD
>>>>>>> 2babd3d (Merge branch 'back' of https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102 into back)
=======
=======
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 0938bf0 (Refactor : 로그인시 넘겨주는 데이터 변경 및 프로필 사진 추가)
=======

>>>>>>> 51dde47 (Refactor : requirements.txt 파일 수정 및 url, views 수정사항 적용)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from .serializers import MyTokenObtainPairView
##aaadd
urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
    path('login', views.LoginView.as_view(), name = "LoginView"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
>>>>>>> 1eb4a5e (Refactor : 일요일 신행상황 저장)
=======
    # path('login', views.LoginView.as_view(), name = "LoginView"),
=======
>>>>>>> 51dde47 (Refactor : requirements.txt 파일 수정 및 url, views 수정사항 적용)
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
>>>>>>> 0938bf0 (Refactor : 로그인시 넘겨주는 데이터 변경 및 프로필 사진 추가)
=======
    path('schoolinfo/', views.SchoolInfoView.as_view(), name='schoolinfo'),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9a0c0d9 (feat : 학교이름 검색 기능 구현 - 홍찬기)
=======
    path('findid/', views.FindIDView.as_view(), name='findid'),
>>>>>>> 668c397 (feat : 회원가입정보 subject,userflag 수정)
=======
    path('checkusername/', views.CheckUsernameView.as_view(), name='checkusername'), 
    path('findusername/', views.FindUsernameView.as_view(), name='findusername'),
    path('sendemail/', views.SendSignupEmailView.as_view(), name='sendsignupemail'),
>>>>>>> 25d0df5 (feat: 회원가입에서 이메일 인증메일 보내기 기능 구현 , id 중복체크 기능 완성 - 홍찬기)
=======
    path('check_username/', views.CheckUsernameView.as_view(), name='checkusername'), 
    path('find_username/', views.FindUsernameView.as_view(), name='findusername'),
    path('send_signup_email/', views.SendSignupEmailView.as_view(), name='sendsignupemail'),
    path('send_pw_email/',views.SendPWEmailView.as_view(), name="sendpwemail"),
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> effb278 (feat: 패스워드변경인증 이메일 기능 구현)
=======
    path('change_pw/', views.ChangePWView.as_view(), name="changepw"),
>>>>>>> d2fc3f3 (feat : 비밀번호 초기화 및 변경 기능 구현)
=======
    path('change_pw/', views.ChangePWView.as_view(), name="changepw"),
>>>>>>> 4eef746 (feat : homework 에도 비밀번호 변경기능 올려놓음)
]
=======

urlpatterns = [
]
>>>>>>> 9206ccc (feat : 회원가입 기능 구현(어느정도))
