from django.db import models
from accounts.models import UserInfo,SchoolInfo
# Create your models here.

class Notice(models.Model):
    teacher = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    school = models.ForeignKey(SchoolInfo, on_delete=models.CASCADE, related_name="notice_school")
    classification = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    views = models.IntegerField(default=0)

class Files(models.Model):
    notice = models.ForeignKey(Notice, related_name="notice_file" ,on_delete=models.CASCADE)
    atch_file_name = models.CharField(max_length=45, default="")   #ss
    atch_file = models.FileField(blank=True, upload_to='notice/files')  # Field name made lowercase.