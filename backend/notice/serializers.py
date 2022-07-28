import imp
from rest_framework import serializers
from accounts.serializers import UserinfoSerializer
from . import models



# 공지사항 목록 Serializer
class NoticeMainSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Notice
        fields = ['classification','title','created_at', 'teacher']

class NoticeCreateSerializer(serializers.ModelSerializer):
    teacher = UserinfoSerializer(read_only=True)
    class Meta:
        model = models.Notice
        fields = '__all__'

