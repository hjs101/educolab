from requests import request
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from accounts.serializers import TeacherNameSerializer
from accounts.models import SchoolInfo,UserInfo
from .serializers import NoticeMainSerializer
from .models import Notice
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

import os
class NoticeMainView(APIView) :
    
    # permission_classes = (IsAuthenticated,)

    def get(self,req):
    

        # email = req.data['email']
        # password = req.data['password']

        ## 1. request로부터 학교 코드를 받는다.
        
        # schoolCode = SchoolInfo.objects.get(code=req.data['schoolcode'])

        schoolCode = req.data['schoolcode']

        ## 2. 쿼리로 학교 코드가 req에서 받은 학교 코드인 사람이 작성자인 공지사항 목록을 가져온다.
        notices = Notice.objects.select_related()
        print(notices.all())
        # 선생 외래키로 선생 이름 가져오기
        
        # 학교 외래키로 reated_name -> 외래키와 연결된 컬럼 가져오기 school

        
        ## 3. 가져온 목록 반환
        
        res = Response()
        # res.data["res"] = "success"


        return res

class NoticeCreateView(APIView):
    def post(self, req):
        notice = Notice()

        notice.teacher = UserInfo.objects.get(username=req.data['username'])
        notice.school = SchoolInfo.objects.get(code=req.data['schoolcode'])
        notice.classification = req.data['division']
        notice.title = req.data['title']
        notice.content = req.data['content']
        
        files = req.FILES.getlist("files")
        
        
        for file in files:
            
