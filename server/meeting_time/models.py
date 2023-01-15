from django.db import models
from candidate.models import Candidate

# Create your models here.
class MeetingTime(models.Model):
    close_time = models.DateTimeField(verbose_name='время занятое')
    free_time = models.DateTimeField(verbose_name='время свободное')
    candidates = models.ForeignKey(Candidate, verbose_name='Кандидат',on_delete=models.CASCADE)

    def __str__(self):
        return self.candidates

    class Meta:
        verbose_name = 'Выбор времени'
    