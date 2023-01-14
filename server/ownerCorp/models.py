from django.db import models

# Create your models here.
class OwnerCorp(models.Model):
    user_id = models.IntegerField(verbose_name='Id пользователя')
    company_id = models.IntegerField(verbose_name='Id компании')

    