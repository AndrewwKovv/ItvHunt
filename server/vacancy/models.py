from django.db import models

# Create your models here.
class Vacancy(models.Model):
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add = True)
    title = models.CharField(verbose_name='Название вакансии', max_length=255)
    link_vacancy = models.TextField(verbose_name='Ссылка')
    candidates_vacancy = models.TextField(verbose_name='Кандидат')
