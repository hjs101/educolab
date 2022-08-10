from django.db import models
from accounts.models import UserInfo
class QuizList(models.Model):
    teacher = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="quiz_teacher")
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

<<<<<<< HEAD
<<<<<<< HEAD
=======
class QuizQuestions(models.Model):
    survey = models.ForeignKey(QuizList, on_delete=models.CASCADE, related_name="question_quiz")
    question_number = models.IntegerField()
    quiz_question = models.CharField(max_length=500)
    multiple_bogi = models.CharField(max_length=500)
    answer = models.IntegerField()
<<<<<<< HEAD
>>>>>>> cc4ab69 (Fix : 퀴즈 기능 모델 오류)

class QuizQuestions(models.Model):
    quiz = models.ForeignKey(QuizList, on_delete=models.CASCADE, related_name="question_quiz")
    question_number = models.IntegerField()
    quiz_question = models.CharField(max_length=500)
    multiple_bogi = models.CharField(max_length=500)
    answer = models.IntegerField()
<<<<<<< HEAD
=======
class QuizQuestions(models.Model):
    survey = models.ForeignKey(QuizList, on_delete=models.CASCADE, related_name="question_quiz")
    question_number = models.IntegerField()
    quiz_question = models.CharField(max_length=500)
    multiple_bogi = models.CharField(max_length=500)
    answer = models.IntegerField()
>>>>>>> f25ab0c (Fix : AWS 파일 옮기기)
=======
>>>>>>> cc4ab69 (Fix : 퀴즈 기능 모델 오류)
=======
>>>>>>> ae59a9c (Feat : 채팅 소켓 진행상황 저장저)
