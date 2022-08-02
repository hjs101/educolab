import imp
from rest_framework import serializers
from accounts.serializers import SchoolInfoSerializer,UserNameSerializer
from . import models



# 공지사항 목록 Serializer
class NoticeMainSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    class Meta:
        model = models.Notice
        fields = ['pk','classification','title','updated_at','views','teacher']

class NoticeSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    school = SchoolInfoSerializer(read_only=True)
    class Meta:
        model = models.Notice
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    atch_file = serializers.FileField(use_url=True)
    
    class Meta:
        model = models.Files
        fields = '__all__'
