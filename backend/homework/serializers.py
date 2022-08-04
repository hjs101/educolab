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

class SubmitHomeworkSerializer(serializers.ModelSerializer):
    student = UserNameSerializer(read_only=True)
    class Meta:
        model = SubmitHomework
        fields = ('student','content','submit_at','submit_flag','atch_file_name','atch_file')

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
        fields = ('id','teacher','title','subject','content','updated_at','deadline','check_flag','student_submit','teacher_file')

class StudentHomeworkDetailSerializer(serializers.ModelSerializer):
    student = UserNameSerializer(read_only=True)
    my_submit = SubmitHomeworkSerializer(many=True,read_only=True)
    student_file = FileSerializer(many=True,read_only=True)
    class Meta:
        model = StudentHomework
        fields = ('id','student','title','content','updated_at','deadline','agreement','student_file','my_submit',)
