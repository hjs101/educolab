import imp
from rest_framework import serializers
from accounts.serializers import SchoolInfoSerializer,TeacherNameSerializer
from . import models



# 공지사항 목록 Serializer
class NoticeMainSerializer(serializers.ModelSerializer):
    teacher = TeacherNameSerializer(read_only=True)
    class Meta:
        model = models.Notice
        fields = ['pk','classification','title','created_at','views','teacher']

class NoticeCreateSerializer(serializers.ModelSerializer):
    teacher = TeacherNameSerializer(read_only=True)
    school = SchoolInfoSerializer(read_only=True)
    class Meta:
        model = models.Notice
        fields = '__all__'

