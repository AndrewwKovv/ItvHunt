# Generated by Django 4.1.4 on 2023-01-17 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0007_alter_task_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTask',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='время создания')),
                ('update_at', models.DateTimeField(blank=True, editable=False, verbose_name='время обновления')),
                ('title', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('desc', models.TextField(verbose_name='Задача')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Ответ')),
                ('language', models.CharField(choices=[('PY', 'PY'), ('JS', 'JS'), ('PHP', 'PHP'), ('HTML', 'HTML')], default='PY', max_length=255, verbose_name='Выбор языка')),
                ('completed', models.BooleanField(default=False, verbose_name='Завершение')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Задача',
                'verbose_name_plural': 'historical Задачи',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]