from django.db import models

# Create your models here.

class Notice(models.Model):
    notice_pk = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    classification = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=10000, blank=True, null=True)
    atch_data_slp = models.CharField(db_column='ATCH_DATA_SLP', max_length=500, blank=True, null=True)  # Field name made lowercase.
    atch_file_name = models.CharField(db_column='ATCH_FILE_NAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    atch_file_size = models.IntegerField(db_column='ATCH_FILE_SIZE', blank=True, null=True)  # Field name made lowercase.
    views = models.IntegerField()