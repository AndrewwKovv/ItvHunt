from django.db import models
from candidate.models import Candidate
from simple_history.models import HistoricalRecords



# Create your models here.
class MeetingTime(models.Model):
    title = models.CharField(verbose_name='Название встречи', max_length=255, null=True)
    free_time = models.DateTimeField(verbose_name='время свободное')
    candidates = models.ManyToManyField(Candidate, verbose_name='Кандидаты', related_name='meetingTimes', blank=True)
    history = HistoricalRecords()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Выбор времени'
