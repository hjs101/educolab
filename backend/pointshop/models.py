from django.db import models

# Create your models here.
class PTitle(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    content = models.CharField(max_length=50,blank=True)

class Icon(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    content = models.CharField(max_length=50,blank=True)
    icon = models.ImageField(upload_to='pointshop/icon/')