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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


>>>>>>> 9206ccc (feat : 회원가입 기능 구현(어느정도))
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
>>>>>>> da408e3 (Feat : 백엔드 Swagger 적용)

urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
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
    path('accounts/', include('accounts.urls')), 
    path('admin/', admin.site.urls),
    path('notice/', include('notice.urls')),
<<<<<<< HEAD
>>>>>>> 601cae8 (Feat : 공지사항 기능 구현)
=======
    path('survey/', include('survey.urls')),
>>>>>>> dfc8ff1 (Feat : 설문조사 생성 기능 구현)
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
