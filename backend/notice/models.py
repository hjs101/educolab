from django.db import models

# Create your models here.

class Notice(models.Model):
<<<<<<< HEAD
    notice_pk = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
=======
    teacher = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    school = models.ForeignKey(SchoolInfo, on_delete=models.CASCADE, related_name="notice_school")
>>>>>>> 3b6b3c2 (Feat : 공지사항 기능 중간 저장)
    classification = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    views = models.IntegerField(default=0)

class Files(models.Model):
<<<<<<< HEAD
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
=======
    notice = models.ForeignKey(Notice, related_name="notice_file" ,on_delete=models.CASCADE)
    atch_file_name = models.CharField(max_length=45, default="")   #ss
>>>>>>> 0101dc7 (Fix : 코드 복구)
    atch_file = models.FileField(blank=True, upload_to='notice/files')  # Field name made lowercase.