from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer
# Create your views here.

class MainpageView(APIView): # 메인페이지 정보 전달 (과제,공지,행사,시간표,랭킹(누적,지난주 랭킹))
    pass

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

class TimelineView(APIView): # 시간표 등록,수정,삭제
    pass

