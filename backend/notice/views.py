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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)
from accounts.serializers import TeacherNameSerializer
from accounts.models import SchoolInfo,UserInfo
from .serializers import NoticeMainSerializer, NoticeCreateSerializer
=======
from accounts.models import SchoolInfo
from .serializers import NoticeMainSerializer, NoticeSerializer,FileSerializer
>>>>>>> c5da375 (Feat : 공지사항 상세페이지 파일 표시, 수정기능(진행중))
=======
from accounts.serializers import TeacherNameSerializer
from accounts.models import SchoolInfo,UserInfo
from .serializers import NoticeMainSerializer, NoticeCreateSerializer
>>>>>>> 559df98 ( Feat : 버그 수정)
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
        # schoolCode = req.GET['schoolcode']

        ## 2. 쿼리로 학교 코드가 req에서 받은 학교 코드인 사람이 작성자인 공지사항 목록을 가져온다.
        school = SchoolInfo.objects.get(code=req.user.school.code)
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
<<<<<<< HEAD

<<<<<<< HEAD

        return res
=======
=======
>>>>>>> c5da375 (Feat : 공지사항 상세페이지 파일 표시, 수정기능(진행중))
=======

>>>>>>> 559df98 ( Feat : 버그 수정)
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

<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
            
>>>>>>> 3b6b3c2 (Feat : 공지사항 기능 중간 저장)
=======
            fp = Files.objects.create(notice=notice[0], atch_file=file)
=======
            fp = Files.objects.create(notice=notice, atch_file=file)
>>>>>>> 1e437b7 (Feat : 공지사항 수정기능 구현)
            fp.save()
<<<<<<< HEAD

        return Response("success")
>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)
=======
        res = Response()
        res.data = {
            'message' : "success",
        }
<<<<<<< HEAD
        return res
>>>>>>> c5da375 (Feat : 공지사항 상세페이지 파일 표시, 수정기능(진행중))
=======
        return Response(notice_serializer.data)
>>>>>>> 1e437b7 (Feat : 공지사항 수정기능 구현)
=======
        return Response("success")
>>>>>>> 559df98 ( Feat : 버그 수정)
