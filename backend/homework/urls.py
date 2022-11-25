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
    path('check/', views.HomeworkCheckView.as_view(), name='homework_check'),
    path('check/done/', views.HomeworkCheckDoneView.as_view()),
    path('submit/', views.HomeworkSubmitView.as_view(), name='homework_submit'),
]
