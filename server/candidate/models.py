from django.db import models
from authentication.models import User

# Create your models here.
class Candidate(models.Model):
    user_email = models.ForeignKey(User, verbose_name='Почта кандидата', on_delete=models.CASCADE, related_name='candidate')
    created_at = models.DateField(verbose_name='Время создания')
    stage = models.TextField(verbose_name='Стадия')

    def __str__(self):
        return self.user_email

    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'
    