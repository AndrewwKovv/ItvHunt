# Generated by Django 4.1.4 on 2023-01-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0009_alter_vacancy_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalvacancy',
            name='created_at',
            field=models.DateField(blank=True, editable=False, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Время создания'),
        ),
    ]
