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
from django.contrib import admin
<<<<<<< HEAD
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg       import openapi
from rest_framework import permissions
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
=======
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg       import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 1d03a62 (Backend file 삽입)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


<<<<<<< HEAD
>>>>>>> 9206ccc (feat : 회원가입 기능 구현(어느정도))
=======
>>>>>>> 1d03a62 (Backend file 삽입)
schema_view = get_schema_view(
    openapi.Info(
        title="EduColab",
        default_version='1.1.1',
        description="EduColab API 문서",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
<<<<<<< HEAD
>>>>>>> da408e3 (Feat : 백엔드 Swagger 적용)

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
=======
    path('accounts/registration', include('dj_rest_auth.registration.urls')),
>>>>>>> 559df98 ( Feat : 버그 수정)
    path('accounts/', include('accounts.urls')), 
    path('admin/', admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path('accounts/',include('accounts.urls'))
=======
>>>>>>> 9b06d95 (feat : 회원가입기능 수정중 - 홍찬기)
=======
    path('accounts/registration', include('dj_rest_auth.registration.urls')),
=======
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
>>>>>>> 77bd03f (feat : get에서  정보 받는 방식 변경)
=======
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
>>>>>>> 69838d6 (Fix : 오류 수정)
=======
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
>>>>>>> d2fc3f3 (feat : 비밀번호 초기화 및 변경 기능 구현)
=======
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
>>>>>>> 82b6b8b (feat : 과제 생성,수정,삭제,상세보기 기능 완성)
    path('accounts/', include('accounts.urls')), 
    path('admin/', admin.site.urls),
    path('notice/', include('notice.urls')),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 601cae8 (Feat : 공지사항 기능 구현)
=======
    path('survey/', include('survey.urls')),
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dfc8ff1 (Feat : 설문조사 생성 기능 구현)
=======
    path('homework/', include('homework.urls')),
<<<<<<< HEAD
>>>>>>> 143f316 (feat: homework 모델변경)
=======
    path('survey/', include('survey.urls')),
    path('homework/', include('homework.urls')),
>>>>>>> 7306741 (feat : 과제 제출 기능 구현)
=======
    path('homework/', include('homework.urls')),
>>>>>>> 0e40bf0 (Fix : 배포관련수정)
=======
    path('survey/', include('survey.urls')),
>>>>>>> 2121f86 (Fix : URL 충돌 해결)
=======
    path('mypage/', include('mypage.urls')),
>>>>>>> 40812b7 (Feat : Mypage 생성)
=======
    path(r'api/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'api/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'api/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
=======
>>>>>>> 3c21bc9 (feat : 과제 정렬, 메인페이지 정보 전달 진행중 누락된게 있어 merge후 진행예정)
=======
    path(r'api/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'api/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'api/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
>>>>>>> 8d76cce (feat : merge중 오류 해결)
    path('api/accounts/registration/', include('dj_rest_auth.registration.urls')),
    path('api/accounts/', include('accounts.urls')), 
    path('api/admin/', admin.site.urls),
    path('api/notice/', include('notice.urls')),
    path('api/homework/', include('homework.urls')),
    path('api/survey/', include('survey.urls')),
    path('api/mypage/', include('mypage.urls')),
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d215d15 (자동배포로 인한 Url 변경)
=======
    path('main/', include('mainpage.urls')),
>>>>>>> 9d68f0e (feat : 메인페이지 학교행사 생성,수정,삭제 기능 구현)
=======
    path('api/main/', include('mainpage.urls')),
<<<<<<< HEAD
>>>>>>> 3c21bc9 (feat : 과제 정렬, 메인페이지 정보 전달 진행중 누락된게 있어 merge후 진행예정)
=======
    path('api/main/', include('mainpage.urls')),
>>>>>>> 8d76cce (feat : merge중 오류 해결)
=======
=======
    path('api/mainpage/', include('mainpage.urls')),
>>>>>>> 1d035b5 (feat: 이달랭킹 및 메인페이지 버그수정)
    path('api/quiz/', include('quiz.urls')),
<<<<<<< HEAD
>>>>>>> 31efb28 (Feat : 퀴즈 기능 구현)
=======
    path('api/pointshop/', include('pointshop.urls')),
>>>>>>> 4910d64 (feat : 상점 기능 구현, 마이페이지 칭호 변경 구현)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

<<<<<<< HEAD
=======
    path('account/',include('accounts.urls'))
=======
    path('accounts/',include('accounts.urls'))
>>>>>>> 9c14433 (Refactor : 로그인 마무리)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 0938bf0 (Refactor : 로그인시 넘겨주는 데이터 변경 및 프로필 사진 추가)
=======
>>>>>>> 51dde47 (Refactor : requirements.txt 파일 수정 및 url, views 수정사항 적용)
=======
]
>>>>>>> 9206ccc (feat : 회원가입 기능 구현(어느정도))
=======

urlpatterns = [
=======
>>>>>>> fc9ea5f (머지)
    path(r'api/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'api/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'api/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    path('api/accounts/registration/', include('dj_rest_auth.registration.urls')),
    path('api/accounts/', include('accounts.urls')), 
    path('api/admin/', admin.site.urls),
    path('api/notice/', include('notice.urls')),
    path('api/homework/', include('homework.urls')),
    path('api/survey/', include('survey.urls')),
    path('api/mypage/', include('mypage.urls')),
<<<<<<< HEAD
=======
    path('api/main/', include('mainpage.urls')),
>>>>>>> fc9ea5f (머지)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

>>>>>>> 1d03a62 (Backend file 삽입)
