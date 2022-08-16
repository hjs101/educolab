<<<<<<< HEAD
#-*-coding: utf-8-*-
=======
>>>>>>> 1d03a62 (Backend file 삽입)
"""
Django settings for educolab project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
##
from pathlib import Path
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import my_settings
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9206ccc (feat : 회원가입 기능 구현(어느정도))
from datetime import timedelta
<<<<<<< HEAD

=======
import datetime
>>>>>>> 1eb4a5e (Refactor : 일요일 신행상황 저장)
=======
from datetime import timedelta
<<<<<<< HEAD

>>>>>>> e82d912 (Repactor : 로그인 기능  simple jwt 변경사항)
=======
from sshtunnel import SSHTunnelForwarder
>>>>>>> 834c26a (Fix : mySettings.py 수정)
=======
import os
>>>>>>> 3b6b3c2 (Feat : 공지사항 기능 중간 저장)
=======
from datetime import timedelta
import os
>>>>>>> c4ffe2e (feat: 회원가입기능 유저플래그수정, 과목추가 - 홍찬기)
=======
from datetime import timedelta
import os
import environ
>>>>>>> 82b6b8b (feat : 과제 생성,수정,삭제,상세보기 기능 완성)
=======
from datetime import timedelta
import os
import environ
>>>>>>> b9da983 (Feat : mypage 구현중)
=======
from datetime import timedelta
import os
import environ
>>>>>>> 1d03a62 (Backend file 삽입)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'api/media/'
<<<<<<< HEAD
=======
MEDIA_URL = '/media/'
>>>>>>> 1d03a62 (Backend file 삽입)
=======
>>>>>>> fc9ea5f (머지)

STATIC_ROOT = '/static/'

env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
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
    'rest_framework_simplejwt',
>>>>>>> 1eb4a5e (Refactor : 일요일 신행상황 저장)
=======
>>>>>>> e82d912 (Repactor : 로그인 기능  simple jwt 변경사항)
=======
=======
    'mypage',
>>>>>>> 40812b7 (Feat : Mypage 생성)
=======
>>>>>>> b9da983 (Feat : mypage 구현중)
=======
=======
=======
>>>>>>> 629f87c (Feat : 채팅)
    'channels',
    'mypage',
    'chat',
<<<<<<< HEAD
>>>>>>> ce3d1c2 (채팅 실습해보기)
=======
>>>>>>> 629f87c (Feat : 채팅)
    'quiz',
>>>>>>> 31efb28 (Feat : 퀴즈 기능 구현)
    'survey',
    'notice',
>>>>>>> d002568 (Feat : 설문조사 App 추가)
    'accounts',
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
    'accounts',
>>>>>>> 9e2d7fd (Style : UserInfo DB 등록)
=======
    'homework',
<<<<<<< HEAD
>>>>>>> 143f316 (feat: homework 모델변경)
=======
    'homework',
>>>>>>> b9da983 (Feat : mypage 구현중)
=======
    'mainpage',
<<<<<<< HEAD
>>>>>>> 9d68f0e (feat : 메인페이지 학교행사 생성,수정,삭제 기능 구현)
=======
    'pointshop',
>>>>>>> 4910d64 (feat : 상점 기능 구현, 마이페이지 칭호 변경 구현)
    'drf_yasg',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> da408e3 (Feat : 백엔드 Swagger 적용)
=======
=======
    'django.contrib.sites',
    'allauth',
    'allauth.account',
>>>>>>> 2babd3d (Merge branch 'back' of https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102 into back)
=======
    'django.contrib.sites',
    'allauth',
    'allauth.account',
>>>>>>> 9206ccc (feat : 회원가입 기능 구현(어느정도))
=======
=======
    'mypage',
>>>>>>> fc9ea5f (머지)
    'survey',
    'notice',
    'accounts',
    'homework',
<<<<<<< HEAD
=======
    'mainpage',
>>>>>>> fc9ea5f (머지)
    'drf_yasg',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
>>>>>>> 1d03a62 (Backend file 삽입)
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'corsheaders',
<<<<<<< HEAD
>>>>>>> e121457 (Refactor : DB수정 후 로그인 변경사항)
=======
=======
    'django.contrib.sites',
    'allauth',
    'allauth.account',
>>>>>>> e82d912 (Repactor : 로그인 기능  simple jwt 변경사항)
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'dj_rest_auth.registration',
    'corsheaders',
>>>>>>> 042ca24 (Feat : 프론트와 연결 가능하게 cors 추가)
=======
>>>>>>> 1d03a62 (Backend file 삽입)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

ASGI_APPLICATION = 'educolab.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'educolab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'educolab.wsgi.application'

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES={
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': env('DB_NAME'),
'USER': env('DB_USER'),
'PASSWORD': env('DB_PASSWORD'),
"HOST": env('DB_HOST'),
"PORT": env('DB_PORT'),
}
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
AUTH_USER_MODEL = 'accounts.User' 
=======
=======
>>>>>>> 1d03a62 (Backend file 삽입)
AUTH_USER_MODEL = 'accounts.UserInfo'

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = True

# 우선 모두 연결해 놓았습니다.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
CORS_ALLOW_ALL_ORIGINS = True
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e121457 (Refactor : DB수정 후 로그인 변경사항)
=======
AUTH_USER_MODEL = 'accounts.UserInfo'
>>>>>>> 9e2d7fd (Style : UserInfo DB 등록)
=======
AUTH_USER_MODEL = 'accounts.UserInfo'

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = True

# 우선 모두 연결해 놓았습니다.
CORS_ALLOW_ALL_ORIGINS = True
<<<<<<< HEAD
>>>>>>> 042ca24 (Feat : 프론트와 연결 가능하게 cors 추가)
=======

REST_FRAMEWORK = {
=======

REST_FRAMEWORK = {
<<<<<<< HEAD
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
>>>>>>> 1eb4a5e (Refactor : 일요일 신행상황 저장)
=======
>>>>>>> e82d912 (Repactor : 로그인 기능  simple jwt 변경사항)
=======

REST_FRAMEWORK = {
>>>>>>> 9206ccc (feat : 회원가입 기능 구현(어느정도))
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
<<<<<<< HEAD
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
=======
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.IsAuthenticated'
    ],
>>>>>>> 601cae8 (Feat : 공지사항 기능 구현)
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9206ccc (feat : 회원가입 기능 구현(어느정도))
=======
=======
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://192.168.0.15:8080",
    "https://i7c102.p.ssafy.io",
    "118.222.223.154"
]
=======
CORS_ALLOW_ORIGINS_ALL = True
>>>>>>> be0df67 (fix : 우선 다시 연결)
=======
=======
>>>>>>> a550878 (feat : 쿠키 보내기, fix: 과제 로그에도 가진 포인트 추가)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "https://i7c102.p.ssafy.io"
]
<<<<<<< HEAD
>>>>>>> 3d9bf43 (fix : cors 적용)
=======

>>>>>>> a550878 (feat : 쿠키 보내기, fix: 과제 로그에도 가진 포인트 추가)

CORS_ALLOW_CREDENTIALS = True
>>>>>>> 4f92e2a (fix : 다양한 기능 수정)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.IsAuthenticated'
    ],
}

>>>>>>> 1d03a62 (Backend file 삽입)
REST_USE_JWT = True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
    'USER_ID_FIELD': 'username',

    'AUTH_COOKIE': 'refresh_token',
    'AUTH_COOKIE_DOMAIN': None,
    'AUTH_COOKIE_SECURE': False,
    'AUTH_COOKIE_HTTP_ONLY': True,
    'AUTH_COOKIE_PATH': '/',
    'AUTH_COOKIE_SAMESITE': 'Lax'
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'
<<<<<<< HEAD
>>>>>>> 2babd3d (Merge branch 'back' of https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102 into back)
=======
=======
REST_USE_JWT = True

>>>>>>> e82d912 (Repactor : 로그인 기능  simple jwt 변경사항)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
    'USER_ID_FIELD': 'username',
}
<<<<<<< HEAD
>>>>>>> 1eb4a5e (Refactor : 일요일 신행상황 저장)
=======

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}
ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'
>>>>>>> e82d912 (Repactor : 로그인 기능  simple jwt 변경사항)
=======
ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'
>>>>>>> 9206ccc (feat : 회원가입 기능 구현(어느정도))
=======

ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'
>>>>>>> 02ef900 (feat : 회원가입기능 학교모델 추가)
=======
ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'
>>>>>>> 834c26a (Fix : mySettings.py 수정)
=======
=======
ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'
>>>>>>> 1d03a62 (Backend file 삽입)

# email
# 메일을 보내는 호스트 서버
EMAIL_HOST = 'smtp.gmail.com'

# ENAIL_HOST에 정의된 SMTP 서버가 사용하는 포트 (587: TLS/STARTTLS용 포트)
EMAIL_PORT = '587'

#  발신할 이메일 주소 '~@gmail.com'
EMAIL_HOST_USER = env('EMAIL_HOST_USER')

# 발신할 이메일 비밀번호 (2단계 인증일경우 앱 비밀번호)
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# TLS 보안 방법 (SMPT 서버와 통신할 떄 TLS (secure) connection 을 사용할지 말지 여부)
EMAIL_USE_TLS = True

# 사이트와 관련한 자동응답을 받을 이메일 주소
<<<<<<< HEAD
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
>>>>>>> 25d0df5 (feat: 회원가입에서 이메일 인증메일 보내기 기능 구현 , id 중복체크 기능 완성 - 홍찬기)
=======
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
>>>>>>> 1d03a62 (Backend file 삽입)
