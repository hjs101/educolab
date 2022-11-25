from django.db import models
from accounts.models import UserInfo
class SurveyList(models.Model):
    teacher = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="survey_teacher")
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    grade = models.IntegerField()
    class_field = models.IntegerField()  # Field renamed because it was a Python reserved
    target = models.ManyToManyField(UserInfo, related_name="target")
    done_target = models.ForeignKey(UserInfo, null=True ,on_delete=models.CASCADE, related_name="target_done")


class SurveyQuestions(models.Model):
    survey = models.ForeignKey(SurveyList, on_delete=models.CASCADE, related_name="question_survey")
    question_number = models.IntegerField()
    survey_question = models.CharField(max_length=500)
    multiple_bogi = models.CharField(max_length=500, blank=True, null=True)
    num1 = models.IntegerField(default=0)
    num2 = models.IntegerField(default=0)
    num3 = models.IntegerField(default=0)
    num4 = models.IntegerField(default=0)
    num5 = models.IntegerField(default=0)

class SurveyQuestionsAnswer(models.Model):
    survey_question_pk = models.ForeignKey('SurveyQuestions',on_delete=models.CASCADE)
    content = models.TextField()

class SueveyTemplate(models.Model):
    teacher_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    data = models.CharField(max_length=450)