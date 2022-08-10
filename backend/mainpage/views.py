from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response

from accounts.models import UserInfo, PointLog
from homework.models import TeacherHomework

from .models import Event, TimeLine
from notice.models import Notice
from .serializers import AccRankSerializer, EventSerializer, MainpageNoticeSerializer, MainpageTHomeworkSerializer, MainpageTeacherhomeworkSerializer, TimelineSerializer
from notice.serializers import NoticeMainSerializer

from datetime import datetime
from django.db.models import Sum
# Create your views here.

class MainpageView(APIView): # 메인페이지 정보 전달 (과제,공지,행사,시간표,랭킹(누적,지난주 랭킹))
    def get(self, request):
        # 행사
        event = Event.objects.filter(school=request.user.school)
        event_serializer = EventSerializer(event, many=True)

        # 공지
        notice = Notice.objects.filter(school=request.user.school)[:5]
        notice_serializer = MainpageNoticeSerializer(notice, many=True)

        # 누적랭킹
        accrank = UserInfo.objects.filter(school=request.user.school).order_by('-acc_point')[:5]
        accrank_serializer = AccRankSerializer(accrank, many=True)
        
        # 이달 랭킹
        today = datetime.now().date()
        this_month = today.month - 1
        if this_month == 0:
            this_month = 12

        pointlog = PointLog.objects.filter(created_at__month=this_month).values("student").annotate(score=Sum("point")).order_by('-score')[:5]
        print(pointlog)

        user = request.user
        if request.user.userflag == True: # 선생님

            # 과제
            homework = user.T_homework.filter(deadline__gt=today).order_by('deadline')
            homework_serializer = MainpageTHomeworkSerializer(homework, many=True)

            context = {
                "event" : event_serializer.data,
                "notice" : notice_serializer.data,
                "acc_rank" : accrank_serializer.data,
                "month_rank" : pointlog,
                "homework" : homework_serializer.data
            }


        else: # 학생
            # 과제
            homework = user.T_homework.filter(deadline__gt=today).order_by('deadline')
            homework_serializer = MainpageTeacherhomeworkSerializer(homework, many=True)
            
            context = {
                "event" : event_serializer.data,
                "notice" : notice_serializer.data,
                "acc_rank" : accrank_serializer.data,
                "month_rank" : pointlog,
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