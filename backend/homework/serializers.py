from rest_framework import serializers
from .models import SubmitHomework, TeacherHomework, StudentHomework, Files
from accounts.serializers import UserNameSerializer, HomeworkUserSerializer

class TeacherHomeworkCreateSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    target = UserNameSerializer(read_only=True,many=True)

    class Meta:
        model = TeacherHomework
        fields = '__all__'

class StudentHomeworkCreateSerializer(serializers.ModelSerializer):
    student = UserNameSerializer(read_only=True)
    teacher = UserNameSerializer(read_only=True)

    class Meta:
        model = StudentHomework
        fields = '__all__'
    
class TeacherHomeworkMainSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherHomework
        fields = ('id','title','deadline','grade','class_field','subject',)

class StudentHomeworkMainSerializer(serializers.ModelSerializer):
    student = HomeworkUserSerializer(read_only=True)
    class Meta:
        model = StudentHomework
        fields = ('id','title','deadline','student',)

<<<<<<< HEAD
class TeacherHomeworkDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherHomework
        fields = ()
=======
class SubmitHomeworkSerializer(serializers.ModelSerializer):
    student = UserNameSerializer(read_only=True)
    class Meta:
        model = SubmitHomework
        fields = ('id','student','content','submit_at','submit_flag','atch_file_name','atch_file')

class SubmitHomeworksubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitHomework
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ('atch_file_name','atch_file')

class TeacherHomeworkDetailSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    teacher_file = FileSerializer(many=True,read_only=True)
    class Meta:
        model = TeacherHomework
<<<<<<< HEAD
<<<<<<< HEAD
        fields = ('id','teacher','grade','class_field','title','subject','content','updated_at','deadline','check_flag','student_submit','teacher_file')
=======
        fields = ('id','teacher','title','subject','content','updated_at','deadline','check_flag','teacher_file')
>>>>>>> 373b6d1 (feat: 과제 생성 기능 수정, 상세정보 기능 수정, 제출 수정)
=======
        fields = ('id','teacher','title','subject','content','updated_at','deadline','check_flag','teacher_file','grade','class_field',)
>>>>>>> 1419234 (fix : 과제 학년반 추가)

class StudentHomeworkDetailSerializer(serializers.ModelSerializer):
    student = UserNameSerializer(read_only=True)
    my_submit = SubmitHomeworkSerializer(many=True, read_only=True)
    student_file = FileSerializer(many=True,read_only=True)
    class Meta:
        model = StudentHomework
<<<<<<< HEAD
<<<<<<< HEAD
        fields = ('id','student','title','content','updated_at','deadline','agreement','student_file','my_submit',)
>>>>>>> 82b6b8b (feat : 과제 생성,수정,삭제,상세보기 기능 완성)
=======
        fields = '__all__'
>>>>>>> 3f78ecb (feat : db 모델 수정)
=======
        fields = ('id','student','title','content','updated_at','deadline','agreement','student_file','my_submit',)
>>>>>>> 9857488 (feat: media 수정중)
