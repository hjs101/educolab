from django.db import models
from accounts.models import UserInfo

# Create your models here.
class TeacherHomework(models.Model):
    teacher = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, related_name='T_homework')
    title = models.CharField(max_length=45)
    subject = models.CharField(max_length=45)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateField()
    grade = models.IntegerField()
    class_field = models.IntegerField()  
    target = models.ManyToManyField(UserInfo, related_name='teacher_homework')
    check_flag = models.BooleanField(default=False)

class StudentHomework(models.Model):
    student = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="S_homework")
    teacher = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, related_name="homeroom_T", null=True)
    title = models.CharField(max_length=45)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateField()
    agreement = models.BooleanField(default=False)
    submit_flag = models.BooleanField(default=False)

class Files(models.Model):
    teacher_homework = models.ForeignKey(TeacherHomework,on_delete=models.CASCADE, null=True, related_name='teacher_file')
    student_homework = models.ForeignKey(StudentHomework, on_delete=models.CASCADE,null=True, related_name='student_file')
    atch_file_name = models.CharField(max_length=45, default="")
    atch_file = models.FileField(blank=True, upload_to='homework/create')  # Field name made lowercase.

class SubmitHomework(models.Model):
    student = models.ForeignKey(UserInfo, on_delete=models.CASCADE,null=True,related_name='submit_homework')
    teacher_homework = models.ForeignKey(TeacherHomework, on_delete=models.CASCADE,null=True, related_name='student_submit')
    student_homework = models.ForeignKey(StudentHomework, on_delete=models.CASCADE,null=True, related_name='my_submit')
    content = models.TextField(null=True)
    submit_at = models.DateTimeField(auto_now=True) # 백앤드에서 현재 시간 넣어주기
    submit_flag = models.BooleanField(default=False)
    atch_file_name = models.CharField(max_length=45, default="",null=True)
    atch_file = models.FileField(blank=True, upload_to='homework/submit',null=True)
