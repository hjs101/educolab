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

from rest_framework_simplejwt.views import (
    TokenVerifyView,
)
from .serializers import MyTokenObtainPairView, MyTokenRefreshView
##aaadd
urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login_web/', views.LoginView.as_view()),
	path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('schoolinfo/', views.SchoolInfoView.as_view(), name='schoolinfo'), 
    path('check_username/', views.CheckUsernameView.as_view(), name='checkusername'), 
    path('find_username/', views.FindUsernameView.as_view(), name='findusername'),
    path('send_signup_email/', views.SendSignupEmailView.as_view(), name='sendsignupemail'),
    path('send_pw_email/',views.SendPWEmailView.as_view(), name="sendpwemail"),
    path('change_pw/', views.ChangePWView.as_view(), name="changepw"),
    path('check_pw/', views.CheckPasswordView.as_view(), name='check_pw'),
]
