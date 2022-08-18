import imp
from rest_framework import serializers
from accounts.serializers import UserinfoSerializer, UserNameSerializer
from . import models

<<<<<<< HEAD
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
<<<<<<< HEAD
=======


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
>>>>>>> f25ab0c (Fix : AWS 파일 옮기기)
=======
        
class QuestionUpdateSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)
    class Meta:
        model = models.QuizQuestions
        fields=['question_number', 'quiz_question', 'multiple_bogi','answer', 'quiz']

>>>>>>> b125449 (Refactor : 백엔드 Question update 수정)
