from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response

from accounts.models import UserInfo, PointLog
from homework.models import TeacherHomework

from .models import Event
from notice.models import Notice
<<<<<<< HEAD
from .serializers import AccRankSerializer, EventSerializer, MainpageNoticeSerializer, MainpageTHomeworkSerializer, MainpageTeacherhomeworkSerializer
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e0daa39 (fix : 머지 충돌)
=======
>>>>>>> 1b417af (Feat : 학생 마이페이지 정보 조회, 포인트 내역 구현 중)
=======
>>>>>>> 82536ab (Fix : 병합)
from notice.serializers import NoticeMainSerializer
=======
>>>>>>> cda8e1a (feat : 채점 여부 플래그)
=======
>>>>>>> 9c48d5b (Fix : back branch와 merge 후 충돌 수정2)
=======
>>>>>>> f7e1d76 (Feat : 학생 마이페이지 구현 완료 & 프로필/뱃지/칭호 변경 및 상벌점 부여 기능 진행 중)
=======
from .serializers import AccRankSerializer, EventSerializer, MainpageNoticeSerializer, MainpageTHomeworkSerializer, MainpageTeacherhomeworkSerializer, WeekRankSerializer
from notice.serializers import NoticeMainSerializer
from accounts.serializers import HomeworkUserSerializer

>>>>>>> eb9e382 (fix : 메인페이지 과제에 유저정보 추가)

import datetime
from django.db.models import Sum
# Create your views here.

class MainpageView(APIView): # 메인페이지 정보 전달 (과제,공지,행사,시간표,랭킹(누적,지난주 랭킹))
    def get(self, request):
        # 행사
        event = Event.objects.filter(school=request.user.school)
        event_serializer = EventSerializer(event, many=True)

        # 공지
        notice = Notice.objects.filter(school=request.user.school).order_by('-pk')[:5]
        notice_serializer = MainpageNoticeSerializer(notice, many=True)

        # 누적랭킹
        accrank = UserInfo.objects.filter(school=request.user.school).order_by('-acc_point')[:5]
        accrank_serializer = AccRankSerializer(accrank, many=True)
        
        # 이달 랭킹
        today = datetime.date.today()
        today_num = today.weekday()
        last_day = today_num + 7
        last_week = today - datetime.timedelta(days=last_day)
        final = today - datetime.timedelta(days=today_num+1)

        pointlogs = PointLog.objects.filter(created_at__range=[last_week,final]).values("student").annotate(score=Sum("point")).order_by('-score')[:5]
        for pointlog in pointlogs:
            pointlog["student"] = UserInfo.objects.get(username=pointlog["student"])
        pointlogs_serializer = WeekRankSerializer(pointlogs, many=True)

        user = request.user
        if request.user.userflag == True: # 선생님

            # 과제
            homework = user.T_homework.filter(deadline__gt=today).order_by('deadline')
            homework_serializer = MainpageTHomeworkSerializer(homework, many=True)

            context = {
                "event" : event_serializer.data,
                "notice" : notice_serializer.data,
                "acc_rank" : accrank_serializer.data,
                "week_rank" : pointlogs_serializer.data,
                "homework" : homework_serializer.data
            }


        else: # 학생
            # 과제
            homework = user.teacher_homework.filter(deadline__gt=today).order_by('deadline')
            homework_serializer = MainpageTeacherhomeworkSerializer(homework, many=True)
            
            context = {
                "event" : event_serializer.data,
                "notice" : notice_serializer.data,
                "acc_rank" : accrank_serializer.data,
                "week_rank" : pointlogs_serializer.data,
                "homework" : homework_serializer.data
            }
        
        return Response(context)





class EventView(APIView): # 행사 등록,수정,삭제
    
    def post(self, request): # 생성
        event = EventSerializer(data=request.data)
        if event.is_valid(raise_exception=True):
            event = event.save(school=request.user.school)
            print(event)
            return Response({
                "success" : True,
                "message" : "성공"
            })
    
    def put(self, request):
        event = Event.objects.get(id=request.data.get('id'))
        event_serializer = EventSerializer(instance=event,data=request.data)
        if event_serializer.is_valid(raise_exception=True):
            event_serializer.save()
            return Response({
                "success" : True,
                "message" : "수정 성공"
            })
    
    def delete(self, request):
        event = Event.objects.get(id=request.data.get('id'))
        event.delete()
        return Response({
            "success" : True,
            "message" : "삭제 성공"
        })