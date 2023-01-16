from django.db import models
from authentication.models import User
from vacancy.models import Vacancy

# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(User, verbose_name='id сотрудника', on_delete=models.CASCADE, null=True)
    vacancies = models.ManyToManyField(Vacancy, verbose_name='Вакансии', related_name='Companies')
    title = models.CharField(verbose_name='Название компании', max_length=255)
    created_at = models.DateField(verbose_name='время создания', auto_now_add = True)
    image_company = models.ImageField(verbose_name='фото компании', upload_to='companies', blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
    