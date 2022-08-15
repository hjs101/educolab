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
    path('main/', views.HomeworkMainView.as_view(), name="homework_main"),
    path('create/', views.HomeworkCreateView.as_view(), name="homework_create"),
    path('detail/', views.HomeworkDetailView.as_view(), name='homework_detail_delete_put'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('check/', views.HomeworkCheckView.as_view(), name='homework_check'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('check/done/', views.HomeworkCheckDoneView.as_view(), name='homework_check_done'),
=======
    path('checkdone/', views.HomeworkCheckDoneView.as_view()),
>>>>>>> cda8e1a (feat : 채점 여부 플래그)
=======
    path('check/done/', views.HomeworkCheckDoneView.as_view()),
>>>>>>> 4f92e2a (fix : 다양한 기능 수정)
    path('submit/', views.HomeworkSubmitView.as_view(), name='homework_submit'),
=======
>>>>>>> 1d03a62 (Backend file 삽입)
=======
    path('check/', views.HomeworkCheckView.as_view(), name='homework_check'),
    path('submit/', views.HomeworkSubmitView.as_view(), name='homework_submit'),
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
]
