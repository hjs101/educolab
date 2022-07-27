from rest_framework import serializers
from . import models



# 공지사항 목록 Serializer
class NoticeMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notice
        fields = ['classification','title','created_at']

class NoticeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notice
        fields = '__all__'

