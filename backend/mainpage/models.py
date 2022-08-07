from django.db import models
from accounts.models import SchoolInfo, UserInfo

# Create your models here.
class Event(models.Model):
    school = models.ForeignKey(SchoolInfo, on_delete=models.CASCADE, related_name='school_events')
    title = models.CharField(max_length=20)
    date = models.DateField()

class TimeLine(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='my_timelines')
    title = models.CharField(max_length=20)
    day = models.CharField(max_length=5)
    period = models.IntegerField()