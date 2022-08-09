from django.urls import is_valid_path
from rest_framework.decorators import APIView
from rest_framework.response import Response
from accounts.models import UserInfo
from pointshop.models import PTitle
from accounts.serializers import UserinfoSerializer
from .serializers import PointlogSerializer,TeacherSerializer, StudentSerializer,SearchStudentSerializer
# Create your views here.


class MypageMainView(APIView):
    def get(self,req):
        ## 학생일 경우
        if req.user.userflag == 0:
            score_logs = req.user.point_student.all()
            userinfo_serializer = StudentSerializer(req.user)
            point_serializer = PointlogSerializer(score_logs,many=True)
            return Response({
            'userinfo' : userinfo_serializer.data,
            'point_log' : point_serializer.data
            })
        userinfo_serializer = TeacherSerializer(req.user)
        return Response({'userinfo':userinfo_serializer.data})

    ## 회원정보수정(담임등록 포함)
    def put(self,req):
        if req.user.userflag:
            userinfo_serializer = TeacherSerializer(req.user, data=req.data)
        else:
            userinfo_serializer = StudentSerializer(req.user, data=req.data)
        if userinfo_serializer.is_valid(raise_exception=True):
            userinfo_serializer.save(school = req.user.school, password = req.user.password)
        return Response({
            "success":True,
            "pk" : req.user.username
        })

class PointGrantView(APIView):
    ## 학생 검색 부분
    def get(self,req):
        key = req.GET['search_key']
        users = UserInfo.objects.filter(school = req.user.school, userflag=0,name__contains=key)
        stu_serializer = SearchStudentSerializer(users,many=True)
        return Response(stu_serializer.data)
    ## 포인트 부여 부분
    def put(self,req):
        stu_id = req.data['student']
        # 학생 인스턴스 가져와서 포인트, 누적포인트 증가
        student = UserInfo.objects.get(username=stu_id)
        # 플러스 포인트(true)인지, 마이너스 포인트(false)인지
        flag = req.data['pointflag']
        point = req.data['log']['point']
        if flag:
            student.plus_point += point
            student.acc_point += point
        else:
            student.minus_point += point
        student.save()
        # 포인트 로그에 기록
        
        log_serializer = PointlogSerializer(data=req.data['log'])
        if log_serializer.is_valid(raise_exception=True):
            log_serializer.save(teacher = req.user, student = student)
        return Response({"success":True})

class ProfilChangeView(APIView):
    def put(self,req):
        user = req.user

        user.profil = req.FILES["profil"]
        
        user.save()
        
        return Response({
            "success" : True
        })

class TitleChangeView(APIView):
    def put(self,request):
        user = request.user

        user.wear_title = PTitle.objects.get(id=request.data.get('pk'))

        user.save()

        return Response({
            "success" : True
        })