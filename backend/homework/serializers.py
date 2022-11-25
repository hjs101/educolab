from rest_framework import serializers
from .models import SubmitHomework, TeacherHomework, StudentHomework, Files
from accounts.serializers import UserNameSerializer, HomeworkUserSerializer

class TeacherHomeworkCreateSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    target = HomeworkUserSerializer(read_only=True,many=True)

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
        fields = ('pk','title','deadline','grade','class_field')

class StudentHomeworkMainSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentHomework
        fields = ('pk','title','deadline')

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
        fields = ('student','content','submit_at','submit_flag','atch_file_name','atch_file')

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
    student_submit = SubmitHomeworkSerializer(many=True,read_only=True)
    teacher_file = FileSerializer(many=True,read_only=True)
    class Meta:
        model = TeacherHomework
        fields = ('id','teacher','grade','class_field','title','subject','content','updated_at','deadline','check_flag','student_submit','teacher_file')

class StudentHomeworkDetailSerializer(serializers.ModelSerializer):
    student = UserNameSerializer(read_only=True)
    my_submit = SubmitHomeworkSerializer(many=True,read_only=True)
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
