from django.db import models

# Create your models here.
class Candidate(models.Model):
    user_email = models.DateTimeField(verbose_name='Почта кандидата')
    created_at = models.DateTimeField(verbose_name='Время создания')
    stage = models.TextField(verbose_name='Стадия')
    owner_company = models.TextField(verbose_name='Наличии в компании')
    