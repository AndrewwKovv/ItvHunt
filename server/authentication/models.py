from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authentication.managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Почта', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    bio = models.TextField(verbose_name='о себе')
    activity_role = models.CharField(verbose_name='Деятельность', max_length=255)
    company_title = models.TextField(verbose_name='id компании', default='corp')

    is_active= models.BooleanField(verbose_name='активный пользователь', default=False)
    is_staff= models.BooleanField(verbose_name='персонал', default=False)
    is_superuser= models.BooleanField(verbose_name='админ', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'activity_role', ]

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    