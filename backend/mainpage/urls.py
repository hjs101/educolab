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
    path('',views.MainpageView.as_view(), name='mainpage'),
    path('event/', views.EventView.as_view(), name='event')
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cda8e1a (feat : 채점 여부 플래그)
=======
>>>>>>> 9c48d5b (Fix : back branch와 merge 후 충돌 수정2)
=======
>>>>>>> e0daa39 (fix : 머지 충돌)
]
