from django.db import models
from accounts.models import SchoolInfo, UserInfo

# Create your models here.
class Event(models.Model):
    school = models.ForeignKey(SchoolInfo, on_delete=models.CASCADE, related_name='school_events')
    title = models.CharField(max_length=20)
    date = models.DateField()
