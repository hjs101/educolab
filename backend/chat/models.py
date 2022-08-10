from django.db import models
from accounts.models import UserInfo
from quiz.models import QuizList,QuizQuestions
class QuizRoom(models.Model):
    teacher = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="teacher_room")
    roomnum = models.IntegerField(primary_key=True)
    quiz = models.ForeignKey(QuizList, on_delete=models.CASCADE, related_name="quiz_room")

class QuizUser(models.Model):
    room = models.ForeignKey(QuizRoom, on_delete=models.CASCADE, related_name="room")
    student = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="stu_room")
    score = models.IntegerField(default=0)

class QuizAnswer(models.Model):
    student = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="stu_answer")
    question = models.ForeignKey(QuizQuestions, on_delete=models.CASCADE, related_name="quiz_questions")
    room = models.ForeignKey(QuizRoom, on_delete=models.CASCADE, related_name="room_answer")