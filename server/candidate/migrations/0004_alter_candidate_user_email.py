# Generated by Django 4.1.4 on 2023-01-16 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidate', '0003_alter_candidate_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='user_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Почта кандидата'),
        ),
    ]
