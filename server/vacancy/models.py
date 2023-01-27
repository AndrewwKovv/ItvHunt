from django.db import models
from candidate.models import Candidate
from rest_framework.pagination import PageNumberPagination
from simple_history.models import HistoricalRecords
from rest_framework.response import Response


# Create your models here.
class Vacancy(models.Model):
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add = True)
    title = models.CharField(verbose_name='Название вакансии', max_length=255)
    link_vacancy = models.TextField(verbose_name='Ссылка')
    candidate = models.ManyToManyField(Candidate, related_name='candidates', verbose_name='Кандидат', blank=True)
    history = HistoricalRecords()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['id', 'title']


class LowResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previos': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'vacancies': data
        })
        
