from urllib import response
from requests import request
from rest_framework.decorators import APIView
from rest_framework.response import Response
<<<<<<< HEAD
from rest_framework.permissions import IsAuthenticated 
<<<<<<< HEAD
=======
=======
from rest_framework.permissions import IsAuthenticated
>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)
from accounts.serializers import TeacherNameSerializer
from accounts.models import SchoolInfo,UserInfo
from .serializers import NoticeMainSerializer, NoticeCreateSerializer
from .models import Notice, Files
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import os, io


<<<<<<< HEAD
import os
>>>>>>> 3b6b3c2 (Feat : 공지사항 기능 중간 저장)
=======
>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)
class NoticeMainView(APIView) :
    ## 권한 설정 부분(View단위)
    # permission_classes = (IsAuthenticated,)

<<<<<<< HEAD
    def post(self,req):
    
=======
    def get(self,req):
>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)

<<<<<<< HEAD
        # email = req.data['email']
        # password = req.data['password']

<<<<<<< HEAD
        ## 0. 로그인한 사용자인지 인증(자동?)

        ## 1. request로부터 학교 코드를 받는다.

        ## 2. 쿼리로 학교 코드가 req에서 받은 학교 코드인 사람이 작성자인 공지사항 목록을 가져온다.

=======
=======
>>>>>>> 3494f79 (Feat : 공지사항 등록, 목록 기능 구현)
        ## 1. request로부터 학교 코드를 받는다.
        schoolCode = req.GET['schoolcode']

        ## 2. 쿼리로 학교 코드가 req에서 받은 학교 코드인 사람이 작성자인 공지사항 목록을 가져온다.
        school = SchoolInfo.objects.get(code=schoolCode)
        notices = school.notice_school.all()
        # notices = Notice.objects.select_related('school').filter(school_id=schoolCode)
        
        ## 3. 시리얼라이저 변환
        notice_serializer = NoticeMainSerializer(notices,many=True)

<<<<<<< HEAD

>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)
        ## 3. 가져온 목록 반환

        res = Response()
=======
        ## 4. 가져온 목록 반환
        res = Response(notice_serializer.data)
>>>>>>> 3494f79 (Feat : 공지사항 등록, 목록 기능 구현)


<<<<<<< HEAD

        return res
=======
        return res

class NoticeCreateView(APIView):
    def post(self, req):
        # notice = Notice()
        notice_serializer = NoticeCreateSerializer(data=req.data)
        if notice_serializer.is_valid(raise_exception=True):
            notice_serializer.save(teacher=req.user, school=SchoolInfo.objects.get(code=req.data['school']))

        files = req.FILES.getlist("files")

        notice = Notice.objects.all().order_by("-pk")
        for file in files:
<<<<<<< HEAD
            
>>>>>>> 3b6b3c2 (Feat : 공지사항 기능 중간 저장)
=======
            fp = Files.objects.create(notice=notice[0], atch_file=file)
            fp.save()

        return Response("success")
>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)
