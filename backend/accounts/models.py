from django.db import models

# Create your models here.
class TeacherInfo(models.Model):
    teacher_id = models.CharField(primary_key=True, max_length=45)
    name = models.CharField(max_length=30)
    birthday = models.IntegerField()
    school = models.CharField(max_length=45)
    subject = models.CharField(max_length=45)
    homeroom_teacher_flag = models.IntegerField()
    homeroom_teacher_grade = models.IntegerField(blank=True, null=True)
    homeroom_teacher_class = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=45)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=45)

class StudentInfo(models.Model):
    student_id = models.CharField(primary_key=True, max_length=45)
    name = models.CharField(max_length=30)
    birthday = models.IntegerField()
    school = models.CharField(max_length=45)
    grade = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved 
    student_number = models.IntegerField()
    password = models.CharField(max_length=45)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=45)
    plus_point = models.IntegerField()
    minus_point = models.IntegerField()
