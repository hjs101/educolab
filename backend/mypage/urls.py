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

urlpatterns = [
    path('main/', views.MypageMainView.as_view(), name='mypage_main'),
    path('grant/', views.PointGrantView.as_view(), name='mypage_point'),
    path('profil/', views.ProfilChangeView.as_view(), name='profil_change'),
    path('title/', views.TitleChangeView.as_view(), name='title_change'),
    
<<<<<<< HEAD
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
=======
>>>>>>> fc9ea5f (머지)
]
