from urllib import response
from requests import request
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import TeacherNameSerializer
from accounts.models import SchoolInfo,UserInfo
from .serializers import NoticeMainSerializer, NoticeCreateSerializer
from .models import Notice, Files
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import os, io


class NoticeMainView(APIView) :
    ## 권한 설정 부분(View단위)
    # permission_classes = (IsAuthenticated,)

    def get(self,req):

        ## 1. request로부터 학교 코드를 받는다.
        schoolCode = req.GET['schoolcode']

        ## 2. 쿼리로 학교 코드가 req에서 받은 학교 코드인 사람이 작성자인 공지사항 목록을 가져온다.
        school = SchoolInfo.objects.get(code=schoolCode)
        notices = school.notice_school.all()
        # notices = Notice.objects.select_related('school').filter(school_id=schoolCode)
        
        ## 3. 시리얼라이저 변환
        notice_serializer = NoticeMainSerializer(notices,many=True)

        ## 4. 가져온 목록 반환
        res = Response(notice_serializer.data)


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
            fp = Files.objects.create(notice=notice[0], atch_file=file)
            fp.save()

        return Response("success")
