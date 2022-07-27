from re import L
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SchoolInfoSerializer
from .models import SchoolInfo

# Create your views here.

class SchoolInfoView(APIView):
    
    def get(self, request):
        search = request.data['schoolname']
        school = SchoolInfo.objects.filter(name__contains=search)
        serializer = SchoolInfoSerializer(school,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
