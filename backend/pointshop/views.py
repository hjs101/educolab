from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response

from .models import PTitle
from .serializers import TitleMainSerializer
# Create your views here.

class MainpageView(APIView):
    def get(self, request):
        titles = PTitle.objects.all()
        title = TitleMainSerializer(titles, many=True)
        return Response(title.data)
    
    def post(self, request):
        buy_title = PTitle.objects.get(id=request.data.get('pk'))
        buy_user = buy_title.title_owner.all()
        if request.user in buy_user: 
            return Response({"success" : False, "message" : "이미 구매한 칭호입니다"})
        else:
            if request.user.plus_point < buy_title.price:
                return Response({"success" : False, "message" : "포인트가 모자랍니다"})
            request.user.plus_point -= buy_title.price
            request.user.own_title.add(buy_title)
            request.user.save()
            return Response({"success" : True, "message" : "구매가 완료되었습니다"})

