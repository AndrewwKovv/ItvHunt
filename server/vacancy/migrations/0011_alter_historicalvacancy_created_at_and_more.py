# Generated by Django 4.1.4 on 2023-01-22 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0010_alter_historicalvacancy_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalvacancy',
            name='created_at',
            field=models.DateTimeField(blank=True, editable=False, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
    ]
