# Generated by Django 4.1.4 on 2023-01-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_remove_candidate_user_email_candidate_user'),
        ('meeting_time', '0002_alter_meetingtime_options_meetingtime_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingtime',
            name='candidates',
        ),
        migrations.AddField(
            model_name='meetingtime',
            name='candidates',
            field=models.ManyToManyField(related_name='meetingTimes', to='candidate.candidate', verbose_name='Кандидат'),
        ),
    ]
