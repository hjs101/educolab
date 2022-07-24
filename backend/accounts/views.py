from base64 import encode
from tkinter.messagebox import NO
from django.urls import is_valid_path
import jwt, datetime, json

from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from .models import UserInfo
from .serializers import MyTokenObtainPairSerializer, UserinfoSerializer;
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate

# Create your views here.
class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            login_id=request.data.get("id"), password=request.data.get("password")
        )
        if user is not None:
            serializer = UserinfoSerializer(user)
            token = MyTokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)