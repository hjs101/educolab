import imp
from rest_framework import serializers
from accounts.serializers import UserNameSerializer, HomeworkUserSerializer
from .models import QuizRoom, QuizAnswer, QuizUser
from quiz.models import QuizList, QuizQuestions
from quiz.serializers import QuizSerializer
class QuizRoomSerializer(serializers.ModelSerializer):
    teacher = UserNameSerializer(read_only=True)
    quiz = QuizSerializer(read_only = True)
    class Meta:
        model = QuizRoom
        fields = '__all__'

class QuizUserSerializer(serializers.ModelSerializer):
    room = QuizRoomSerializer(read_only=True)
    student = UserNameSerializer(read_only=True)
    class Meta:
        model = QuizUser
        fields = '__all__'