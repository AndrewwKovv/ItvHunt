from django.db import models
from authentication.models import User

# Create your models here.
class Candidate(models.Model):
    INTERVIEW = 'Interview'
    TASK = 'Task'
    ACCEPT = 'Accept'
    REFUSAL = 'Refusal'
    STAGE_CHOICES = [
        (INTERVIEW  ,'Interview'),
        (TASK,'Task'),
        (ACCEPT, 'Accept'),
        (REFUSAL, 'Refusal'),
    ]
    email_candidate = models.EmailField(verbose_name='Почта', max_length=255, null=True)
    # candidate = models.ManyToManyField(User, verbose_name='Кандидат', related_name='candidates')
    created_at = models.DateField(verbose_name='Время создания')
    stage = models.CharField(verbose_name='Стадия', max_length=255, choices=STAGE_CHOICES,default = INTERVIEW)

    def __str__(self):
        return self.email_candidate

    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'
    