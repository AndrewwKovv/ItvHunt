from django.db import models
from candidate.models import Candidate

# Create your models here.
class Vacancy(models.Model):
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add = True)
    title = models.CharField(verbose_name='Название вакансии', max_length=255)
    link_vacancy = models.TextField(verbose_name='Ссылка')
    candidate_id = models.ForeignKey(Candidate , verbose_name='Кандидат', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
