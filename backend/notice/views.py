<<<<<<< HEAD
<<<<<<< HEAD
from rest_framework.decorators import APIView
from rest_framework.response import Response
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from rest_framework.permissions import IsAuthenticated 
<<<<<<< HEAD
=======
=======
from rest_framework.permissions import IsAuthenticated
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)
from accounts.serializers import TeacherNameSerializer
from accounts.models import SchoolInfo,UserInfo
from .serializers import NoticeMainSerializer, NoticeCreateSerializer
=======
=======
>>>>>>> 82a5c7c (feat: pull전 commit)
from accounts.models import SchoolInfo
from .serializers import NoticeMainSerializer, NoticeSerializer,FileSerializer
>>>>>>> c5da375 (Feat : 공지사항 상세페이지 파일 표시, 수정기능(진행중))
=======
from accounts.serializers import TeacherNameSerializer
from accounts.models import SchoolInfo,UserInfo
from .serializers import NoticeMainSerializer, NoticeCreateSerializer
>>>>>>> 559df98 ( Feat : 버그 수정)
=======
from accounts.serializers import TeacherNameSerializer
=======
from accounts.serializers import UserNameSerializer
>>>>>>> ae003cb (Feat : 설문조사 기능 구현)
=======
>>>>>>> b9da983 (Feat : mypage 구현중)
from accounts.models import SchoolInfo,UserInfo
from .serializers import NoticeMainSerializer, NoticeSerializer, FileSerializer
>>>>>>> 417b70e (Fix : 충돌 수정)
from .models import Notice, Files
<<<<<<< HEAD
<<<<<<< HEAD
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import os, io
=======
>>>>>>> 82a5c7c (feat: pull전 commit)
=======
from accounts.models import SchoolInfo
from .serializers import NoticeMainSerializer, NoticeSerializer,FileSerializer
from .models import Notice, Files
>>>>>>> 7306741 (feat : 과제 제출 기능 구현)
=======
from accounts.models import SchoolInfo
from .serializers import NoticeMainSerializer, NoticeSerializer,FileSerializer
from .models import Notice, Files
>>>>>>> 0e40bf0 (Fix : 배포관련수정)
=======
>>>>>>> b9da983 (Feat : mypage 구현중)


<<<<<<< HEAD
import os
>>>>>>> 3b6b3c2 (Feat : 공지사항 기능 중간 저장)
=======
>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)
=======
from urllib import response
from requests import request
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
from rest_framework.decorators import APIView
from rest_framework.response import Response
from accounts.models import SchoolInfo
from .serializers import NoticeMainSerializer, NoticeSerializer,FileSerializer
from .models import Notice, Files


>>>>>>> 1d03a62 (Backend file 삽입)
class NoticeMainView(APIView) :
    ## 권한 설정 부분(View단위)
    # permission_classes = (IsAuthenticated,)

<<<<<<< HEAD
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
=======
    def get(self,req):

>>>>>>> 1d03a62 (Backend file 삽입)
        ## 1. request로부터 학교 코드를 받는다.
        # schoolCode = req.GET['schoolcode']

        ## 2. 쿼리로 학교 코드가 req에서 받은 학교 코드인 사람이 작성자인 공지사항 목록을 가져온다.
        school = SchoolInfo.objects.get(code=req.user.school.code)
        notices = school.notice_school.all().order_by('-updated_at')
        # notices = Notice.objects.select_related('school').filter(school_id=schoolCode)
        
        ## 3. 시리얼라이저 변환
        notice_serializer = NoticeMainSerializer(notices,many=True)

<<<<<<< HEAD
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

<<<<<<< HEAD

        return res
=======
=======
>>>>>>> c5da375 (Feat : 공지사항 상세페이지 파일 표시, 수정기능(진행중))
=======

>>>>>>> 559df98 ( Feat : 버그 수정)
=======

>>>>>>> 417b70e (Fix : 충돌 수정)
=======
        ## 4. 가져온 목록 반환
        res = Response(notice_serializer.data)


>>>>>>> 1d03a62 (Backend file 삽입)
        return res

class NoticeCreateView(APIView):
    def post(self, req):
<<<<<<< HEAD
<<<<<<< HEAD
        print(req.data)
=======
>>>>>>> 1d03a62 (Backend file 삽입)
=======
        print(req.data)
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
        if not req.user.userflag:
            return Response({"message : 선생님만 접근 가능합니다."})
        # notice = Notice()
        notice_serializer = NoticeSerializer(data=req.data)
        if notice_serializer.is_valid(raise_exception=True):
            notice = notice_serializer.save(teacher=req.user, school=SchoolInfo.objects.get(code=req.user.school.code))

        files = req.FILES.getlist("files")
<<<<<<< HEAD
        print(req.data['files'])

        for file in files:
<<<<<<< HEAD
            fp = Files.objects.create(notice=notice[0], atch_file=file, atch_file_name=file)
            fp.save()
        return Response({"success" : True})

<<<<<<< HEAD
=======
=======

        print(files)
        for file in files:
>>>>>>> 1d03a62 (Backend file 삽입)
            fp = Files.objects.create(notice=notice, atch_file=file, atch_file_name=file)
            fp.save()
        return Response({
            "success":True,
            "pk" : notice.pk
        })
<<<<<<< HEAD
>>>>>>> ae003cb (Feat : 설문조사 기능 구현)
=======
>>>>>>> 1d03a62 (Backend file 삽입)
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
<<<<<<< HEAD
<<<<<<< HEAD

=======
        print(files)
>>>>>>> 1d03a62 (Backend file 삽입)
=======

>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
        
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
        if not req.user.userflag:
            return Response({"message : 선생님만 접근 가능합니다."})
        
        notice_id = req.GET['notice_num']

        ## 공지사항 번호로 공지사항 인스턴스 가져오기
        notice = Notice.objects.get(pk=notice_id)
#
        notice.delete()
        return Response("success")

class NoticeUpdateView(APIView):
<<<<<<< HEAD
<<<<<<< HEAD
=======
    notice_id = ""
>>>>>>> 1d03a62 (Backend file 삽입)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    def get(self, req):
        if not req.user.userflag:
            return Response({"message : 선생님만 접근 가능합니다."})
        ## 공지사항 번호 가져오기
<<<<<<< HEAD
<<<<<<< HEAD
        notice_id = req.GET['notice_num']
=======
        self.notice_id = req.GET['notice_num']
>>>>>>> 1d03a62 (Backend file 삽입)
=======
        notice_id = req.GET['notice_num']
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)

        ## 공지사항 번호로 공지사항 인스턴스 가져오기
        notice = Notice.objects.get(pk=notice_id)

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
<<<<<<< HEAD
<<<<<<< HEAD
        notice_id = req.data['notice_num']
        notice = Notice.objects.get(pk=notice_id)
=======
        self.notice_id = req.data['notice_num']
        notice = Notice.objects.get(pk=self.notice_id)
>>>>>>> 1d03a62 (Backend file 삽입)
=======
        notice_id = req.data['notice_num']
        notice = Notice.objects.get(pk=notice_id)
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
        notice_serializer = NoticeSerializer(notice, data=req.data)
        if notice_serializer.is_valid(raise_exception=True):
            print('valid')
            notice = notice_serializer.save(teacher=req.user, school=req.user.school)
            print(notice)
        notice_files = notice.notice_file.all()
        notice_files.delete()

        files = req.FILES.getlist("files")

        for file in files:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            
>>>>>>> 3b6b3c2 (Feat : 공지사항 기능 중간 저장)
=======
            fp = Files.objects.create(notice=notice[0], atch_file=file)
=======
            fp = Files.objects.create(notice=notice, atch_file=file)
>>>>>>> 1e437b7 (Feat : 공지사항 수정기능 구현)
=======
            fp = Files.objects.create(notice=notice, atch_file=file, atch_file_name=file)
>>>>>>> 0101dc7 (Fix : 코드 복구)
=======
            fp = Files.objects.create(notice=notice, atch_file=file, atch_file_name=file)
>>>>>>> ae003cb (Feat : 설문조사 기능 구현)
            fp.save()
<<<<<<< HEAD

        return Response("success")
>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)
=======
        res = Response()
<<<<<<< HEAD
=======
            fp = Files.objects.create(notice=notice, atch_file=file, atch_file_name=file)
            fp.save()
        res = Response()
>>>>>>> 1d03a62 (Backend file 삽입)
        res.data = {
            'success' : True,
            "pk" : notice.pk
        }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return res
>>>>>>> c5da375 (Feat : 공지사항 상세페이지 파일 표시, 수정기능(진행중))
=======
        return Response(notice_serializer.data)
>>>>>>> 1e437b7 (Feat : 공지사항 수정기능 구현)
=======
        return Response("success")
>>>>>>> 559df98 ( Feat : 버그 수정)
=======
        return Response(notice_serializer.data)
>>>>>>> 417b70e (Fix : 충돌 수정)
=======
        return Response({"success":True})
>>>>>>> 5489a10 (Feat : Response 응답 값 수정)
=======
        return res
>>>>>>> ae003cb (Feat : 설문조사 기능 구현)
=======
        return res
>>>>>>> 1d03a62 (Backend file 삽입)
