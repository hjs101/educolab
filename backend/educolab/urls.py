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
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg       import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


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

urlpatterns = [
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
    path('api/mainpage/', include('mainpage.urls')),
    path('api/quiz/', include('quiz.urls')),
    path('api/pointshop/', include('pointshop.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

