from rest_framework import serializers
from accounts.serializers import SchoolInfoSerializer,UserNameSerializer
from . import models



# 공지사항 목록 Serializer
class NoticeMainSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    class Meta:
<<<<<<< HEAD
<<<<<<< HEAD
        model = models.UserInfo
        fields = ['classification','title','created_at','teacher']
=======
        model = models.Notice
<<<<<<< HEAD
        fields = ['pk','classification','title','created_at','views','teacher']
=======
        fields = ['pk','classification','title','updated_at','views','teacher']
>>>>>>> 53d5343 (Feat : 데이터 변경사항 수정)
=======
        model = models.Notice
<<<<<<< HEAD
        fields = ['pk','classification','title','updated_at','views','teacher']
>>>>>>> 1d03a62 (Backend file 삽입)
=======
        fields = ['pk','classification','title','created_at','views','teacher']
>>>>>>> 9f5dc40 (Refactor : 공지사항 기능 수정)

class NoticeSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    school = SchoolInfoSerializer(read_only=True)
    class Meta:
        model = models.Notice
        fields = '__all__'

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 73fd2c6 (Feat : 공지사항 기능 진행상황 저장)
=======
=======
>>>>>>> f99fc5d (Fix : 오류 수정)
=======
>>>>>>> 1d03a62 (Backend file 삽입)
class FileSerializer(serializers.ModelSerializer):
    atch_file = serializers.FileField(use_url=True)
    
    class Meta:
        model = models.Files
        fields = '__all__'
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5da375 (Feat : 공지사항 상세페이지 파일 표시, 수정기능(진행중))
=======
    
=======
>>>>>>> 0970789 (Style : back 브랜치 테스트)

<<<<<<< HEAD
>>>>>>> 1e437b7 (Feat : 공지사항 수정기능 구현)
=======
>>>>>>> 559df98 ( Feat : 버그 수정)
=======
>>>>>>> f99fc5d (Fix : 오류 수정)
=======
>>>>>>> afd284c (Fix : 버그수정)
=======
>>>>>>> 1d03a62 (Backend file 삽입)
