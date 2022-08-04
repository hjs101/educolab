from rest_framework.decorators import APIView
from rest_framework.response import Response
from accounts.models import SchoolInfo,UserInfo

# Create your views here.


class MypageMainView(APIView):
    