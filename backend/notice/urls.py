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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path('main', views.NoticeMainView.as_view(), name='notice/main'),
=======
=======
    # 메인
>>>>>>> 4110506 (공지사항 메인페이지 백 통신 완료)
    path('main/', views.NoticeMainView.as_view(), name='notice/main'),
    path('create/', views.NoticeCreateView.as_view(), name='notice/create'),
>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)
=======
    path('main/', views.NoticeMainView.as_view(), name='notice_main'),
    path('create/', views.NoticeCreateView.as_view(), name='notice_create'),
    path('detail/', views.NoticeDetailView.as_view(), name='notice_detail'),
<<<<<<< HEAD
>>>>>>> c5da375 (Feat : 공지사항 상세페이지 파일 표시, 수정기능(진행중))
=======
    path('update/', views.NoticeUpdateView.as_view(), name='notice_update'),
>>>>>>> 1e437b7 (Feat : 공지사항 수정기능 구현)
=======
    path('main/', views.NoticeMainView.as_view(), name='notice/main'),
    path('create/', views.NoticeCreateView.as_view(), name='notice/create'),
>>>>>>> 559df98 ( Feat : 버그 수정)
=======
    path('main/', views.NoticeMainView.as_view(), name='notice_main'),
    path('create/', views.NoticeCreateView.as_view(), name='notice_create'),
    path('detail/', views.NoticeDetailView.as_view(), name='notice_detail'),
    path('update/', views.NoticeUpdateView.as_view(), name='notice_update'),
>>>>>>> 15da655 (Fix : 버그수정)
]
