from django.db import models

# Create your models here.
class Task(models.Model):
    created_at = models.DateTimeField(verbose_name='время создания', auto_now_add = True)
    update_at = models.DateTimeField(verbose_name='время обновления', auto_now = True)
    title = models.CharField(verbose_name='Название задачи', max_length=255)
    desc = models.TextField(verbose_name='Задача')
    answer = models.TextField(verbose_name='Ответ')
    language = models.CharField(verbose_name='Выбор языка', max_length=255)
    completed = models.BooleanField(verbose_name='Завершение',default = False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'