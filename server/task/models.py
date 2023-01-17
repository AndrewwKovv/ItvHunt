from django.db import models
from  rest_framework.pagination import PageNumberPagination
from simple_history.models import HistoricalRecords


# Create your models here.
class Task(models.Model):
    PYATHON = 'PY'
    JAVASCRIPT = 'JS'
    PHP = 'PHP'
    HTML = 'HTML'
    LANGUAGE_CHOICES = [
        (PYATHON, 'PY'),
        (JAVASCRIPT, 'JS'),
        (PHP,'PHP'),
        (HTML, 'HTML'),
    ]
    created_at = models.DateTimeField(verbose_name='время создания', auto_now_add = True)
    update_at = models.DateTimeField(verbose_name='время обновления', auto_now = True)
    title = models.CharField(verbose_name='Название задачи', max_length=255)
    desc = models.TextField(verbose_name='Задача')
    answer = models.TextField(verbose_name='Ответ', blank=True, null=True)
    language = models.CharField(verbose_name='Выбор языка', max_length=255, choices=LANGUAGE_CHOICES, default = PYATHON)
    completed = models.BooleanField(verbose_name='Завершение', default = False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['id', 'title']



class LowResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000