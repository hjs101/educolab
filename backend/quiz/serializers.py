import imp
from rest_framework import serializers
from accounts.serializers import UserinfoSerializer, UserNameSerializer
from . import models

class QuizMainSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    class Meta:
        model = models.QuizList
        fields = ['pk','title','updated_at','teacher']

class QuizSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    class Meta:
        model = models.QuizList
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)
    class Meta:
        model = models.QuizQuestions
        fields='__all__'

class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizQuestions
        fields= ['id','question_number', 'quiz_question', 'multiple_bogi','answer']