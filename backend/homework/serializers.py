from rest_framework import serializers
from .models import TeacherHomework, StudentHomework
from accounts.serializers import UserNameSerializer, HomeworkUserSerializer

class TeacherHomeworkCreateSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    target = HomeworkUserSerializer(read_only=True,many=True)

    class Meta:
        model = TeacherHomework
        fields = '__all__'

class StudentHomeworkCreateSerializer(serializers.ModelSerializer):
    student = UserNameSerializer(read_only=True)

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