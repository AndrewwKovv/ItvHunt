# Generated by Django 4.1.4 on 2023-01-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('title', models.CharField(max_length=255, verbose_name='Название вакансии')),
                ('link_vacancy', models.TextField(verbose_name='Ссылка')),
                ('candidates_vacancy', models.TextField(verbose_name='Кандидат')),
            ],
        ),
    ]
