from django.db import models

# Create your models here.
class Task(models.Model):
    type = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    title = models.CharField(max_length=30)
    desc = models.TextField()
    answer = models.CharField(max_length=250)
    language = models.CharField(max_length=30)