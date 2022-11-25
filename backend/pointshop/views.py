from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response

from .models import PTitle, Icon
from .serializers import IconMainSerializer, TitleMainSerializer
# Create your views here.

class MainpageView(APIView):
    def get(self, request):
        titles = PTitle.objects.all()
        title = TitleMainSerializer(titles, many=True)
        icons = Icon.objects.all()
        icon = IconMainSerializer(icons, many=True)
        context = {
            "titles" : title.data,
            "icons" : icon.data
        }
        return Response(context)


class PtitleView(APIView):
    
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

class IconView(APIView):

    def post(self, request):
        buy_icon = Icon.objects.get(id=request.data.get('pk'))
        buy_user = buy_icon.icon_owner.all()
        if request.user in buy_user:
            return Response({"success" : False, "message" : "이미 구매한 아이콘입니다"})
        else:
            if request.user.plus_point < buy_icon.price:
                return Response({"success" : False, "message" : "포인트가 모자랍니다"})
            request.user.plus_point -= buy_icon.price
            request.user.own_icon.add(buy_icon)
            request.user.save()

            return Response({"success" : True, "message" : "구매가 완료되었습니다"})


class IconRegisterView(APIView):

    def post(self, request):
        title = request.data.get('title')
        price = request.data.get('price')
        content = request.data.get('content')
        file = request.FILES.get("file")
        icon = Icon.objects.create(title=title,price=price,content=content,icon=file)
        icon.save()

        return Response({"success" : True, "message" : "등록 완료"})
