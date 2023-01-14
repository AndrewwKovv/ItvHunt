from django.db import models

# Create your models here.
class Company(models.Model):
    user_id = models.IntegerField(verbose_name='Id пользователя')
    title = models.CharField(verbose_name='Название компании')
    created_at = models.DateTimeField(verbose_name='время создания', auto_now_add = True)
    image_company = models.CharField(max_length=255)
    