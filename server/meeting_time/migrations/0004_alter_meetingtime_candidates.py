# Generated by Django 4.1.4 on 2023-01-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0010_remove_candidate_candidate'),
        ('meeting_time', '0003_remove_meetingtime_candidates_meetingtime_candidates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingtime',
            name='candidates',
            field=models.ManyToManyField(related_name='meetingTimes', to='candidate.candidate', verbose_name='Кандидаты'),
        ),
    ]
