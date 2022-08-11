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

from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    path('req/answer/', views.AnswerSubmitView.as_view(), name='answer_submit'),
    path('req/scoreadd/', views.ScoreAddView.as_view(), name='score_add'),
    path('req/rank/', views.RankScoreView.as_view(), name='rank'),
    path('req/stu_result/', views.StudentResultView.as_view(), name='stu_result'),
]