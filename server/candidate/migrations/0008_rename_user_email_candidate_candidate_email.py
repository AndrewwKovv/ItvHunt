# Generated by Django 4.1.4 on 2023-01-16 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0007_rename_user_candidate_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='user_email',
            new_name='candidate_email',
        ),
    ]