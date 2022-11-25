from django.db import models
from accounts.models import UserInfo
class QuizList(models.Model):
    teacher = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="quiz_teacher")
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class QuizQuestions(models.Model):
    quiz = models.ForeignKey(QuizList, on_delete=models.CASCADE, related_name="question_quiz")
    question_number = models.IntegerField()
    quiz_question = models.CharField(max_length=500)
    multiple_bogi = models.CharField(max_length=500)
    answer = models.IntegerField()
