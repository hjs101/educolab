from rest_framework import serializers
from accounts.models import UserInfo

from accounts.serializers import SchoolInfoSerializer, HomeworkUserSerializer
from accounts.models import PointLog
from homework.models import StudentHomework, SubmitHomework, TeacherHomework
from .models import Event
from notice.models import Notice

class EventSerializer(serializers.ModelSerializer):
    school = SchoolInfoSerializer(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'

class MainpageNoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = ('classification','title','updated_at',)

class MainpageTHomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherHomework
        fields = ('pk','title','deadline','grade','class_field')

class AccRankSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ('username','name','grade','class_field','acc_point')

class WeekRankSerializer(serializers.Serializer):
    student = HomeworkUserSerializer(read_only=True)
    score = serializers.IntegerField()

class MainpageTeacherhomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherHomework
        fields = ('title','deadline','pk')

class MainpageStudenthomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentHomework
        fields = ('title','deadline','pk')

class MainpageSubmitHomeworkSerializer(serializers.ModelSerializer):
    teacher_homework = MainpageTeacherhomeworkSerializer(read_only=True)
    student_homework = MainpageStudenthomeworkSerializer(read_only=True)

    class Meta:
        model = SubmitHomework
        fields = ('teacher_homework','student_homework',)
