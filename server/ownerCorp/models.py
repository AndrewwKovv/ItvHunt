from django.db import models

# Create your models here.
class OwnerCorp(models.Model):
    user = models.TextField(verbose_name='Id пользователя', null=True)
    company = models.TextField(verbose_name='Id пользователя', null=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Владелец компании'
        verbose_name_plural = 'Владельцы компании'

    