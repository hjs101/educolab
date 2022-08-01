from urllib import response
from requests import request
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import TeacherNameSerializer
from accounts.models import SchoolInfo,UserInfo
from .serializers import NoticeMainSerializer, NoticeSerializer, FileSerializer
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
        # schoolCode = req.GET['schoolcode']

        ## 2. 쿼리로 학교 코드가 req에서 받은 학교 코드인 사람이 작성자인 공지사항 목록을 가져온다.
        school = SchoolInfo.objects.get(code=req.user.school.code)
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
            notice_serializer.save(teacher=req.user, school=SchoolInfo.objects.get(code=req.user.school.code))

        files = req.FILES.getlist("files")

        notice = Notice.objects.all().order_by("-pk")
        for file in files:
            fp = Files.objects.create(notice=notice[0], atch_file=file)
            fp.save()

class NoticeDetailView(APIView):
    def get(self, req):
        ## 공지사항 번호 가져오기
        notice_id = req.GET['notice_num']

        ## 공지사항 번호로 공지사항 인스턴스 가져오기
        notice = Notice.objects.get(pk=notice_id)


        ## 조회수 1 올리기 
        notice.views+=1
        
        notice.save()

        files = notice.notice_file.all()
        
        
        fileserializer = FileSerializer(files, many=True)
        print(files)
        
        ## 공지사항 시리얼라이저 생성
        notice_detail_serializer = NoticeSerializer(notice)
        res = Response()
        res.data = {
            "notice" : notice_detail_serializer.data,
            "files" : fileserializer.data,
        }
        if notice_detail_serializer.data['school']['code'] == req.user.school.code:
            return res

        
        return Response({"message" : "잘못된 접근입니다."})

    def delete(self, req):
        notice_id = req.GET['notice_num']

        ## 공지사항 번호로 공지사항 인스턴스 가져오기
        notice = Notice.objects.get(pk=notice_id)

        notice.delete()
        return Response("success")

class NoticeUpdateView(APIView):
    notice_id = ""
    def get(self, req):
        ## 공지사항 번호 가져오기
        self.notice_id = req.GET['notice_num']

        ## 공지사항 번호로 공지사항 인스턴스 가져오기
        notice = Notice.objects.get(pk=self.notice_id)

        notice.save()

        files = notice.notice_file.all()


        fileserializer = FileSerializer(files, many=True)
        print(files)

        ## 공지사항 시리얼라이저 생성
        notice_detail_serializer = NoticeSerializer(notice)
        res = Response()
        res.data = {
            "notice" : notice_detail_serializer.data,
            "files" : fileserializer.data,
        }
        if notice_detail_serializer.data['school']['code'] == req.user.school.code:
            return res


        return Response({"message" : "잘못된 접근입니다."})

    def put(self, req):
        self.notice_id = req.data['notice_num']
        notice = Notice.objects.get(pk=self.notice_id)
        notice_serializer = NoticeSerializer(notice, data=req.data)
        if notice_serializer.is_valid(raise_exception=True):
            notice_serializer.save(teacher=req.user, school=SchoolInfo.objects.get(code=req.data['school']))

        notice_files = notice.notice_file.all()
        notice_files.delete()

        
        files = req.FILES.getlist("files")

        for file in files:
            fp = Files.objects.create(notice=notice, atch_file=file)
            fp.save()
        res = Response()
        res.data = {
            'message' : "success",
        }
        return Response(notice_serializer.data)
