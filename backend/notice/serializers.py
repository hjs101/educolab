import imp
from rest_framework import serializers
from accounts.serializers import SchoolInfoSerializer,TeacherNameSerializer
from . import models



# 공지사항 목록 Serializer
class NoticeMainSerializer(serializers.ModelSerializer):
    teacher = TeacherNameSerializer(read_only=True)
    class Meta:
<<<<<<< HEAD
        model = models.UserInfo
        fields = ['classification','title','created_at','teacher']
=======
        model = models.Notice
        fields = ['pk','classification','title','created_at','views','teacher']

class NoticeCreateSerializer(serializers.ModelSerializer):
    teacher = TeacherNameSerializer(read_only=True)
    school = SchoolInfoSerializer(read_only=True)
    class Meta:
        model = models.Notice
        fields = '__all__'

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)
=======
class FileSerializer(serializers.ModelSerializer):
    atch_file = serializers.FileField(use_url=True)
    class Meta:
        model = models.Files
        fields = '__all__'
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5da375 (Feat : 공지사항 상세페이지 파일 표시, 수정기능(진행중))
=======
    
=======
>>>>>>> 0970789 (Style : back 브랜치 테스트)

>>>>>>> 1e437b7 (Feat : 공지사항 수정기능 구현)
=======
>>>>>>> 559df98 ( Feat : 버그 수정)
