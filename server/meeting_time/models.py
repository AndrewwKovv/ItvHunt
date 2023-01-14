from django.db import models

# Create your models here.
class MeetingTime(models.Model):
    close_time = models.DateTimeField(verbose_name='время занятое')
    free_time = models.DateTimeField(verbose_name='время свободное')
    candidates = models.TextField(verbose_name='Кандидат')
    