import imp
from rest_framework import serializers
from accounts.serializers import UserinfoSerializer, UserNameSerializer
from . import models



# 설문조사 Serializer
class SurveySerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
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

class SurveyMainSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    class Meta:
        model = models.SurveyList
        fields = ['pk','title','updated_at','grade', 'class_field','teacher']
class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurveyQuestions
        fields= ['id','question_number', 'survey_question', 'multiple_bogi']

class QuestionStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurveyQuestions
        fields = ['id','survey_question','question_number','multiple_bogi','num1','num2','num3','num4','num5']

class QuestionStatDetailSerializer(serializers.ModelSerializer):
    question = QuestionDetailSerializer(read_only=True)
    class Meta:
        model = models.SurveyQuestionsAnswer
        fields = "__all__"

class QuestionsAnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    class Meta:
        model = models.SurveyQuestionsAnswer
        fields = "__all__"