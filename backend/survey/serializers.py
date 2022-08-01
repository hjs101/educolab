import imp
from rest_framework import serializers
from accounts.serializers import UserinfoSerializer, TeacherNameSerializer
from . import models



# 설문조사 Serializer
class SurveySerializer(serializers.ModelSerializer):
    teacher = TeacherNameSerializer(read_only=True)
    target = UserinfoSerializer(read_only=True, many=True)
    done_target = UserinfoSerializer(read_only=True)
    class Meta:
        model = models.SurveyList
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    survey = SurveySerializer(read_only=True)
    class Meta:
        model = models.SurveyQuestions
        fields='__all__'