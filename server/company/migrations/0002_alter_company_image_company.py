# Generated by Django 4.1.4 on 2023-01-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image_company',
            field=models.ImageField(blank=True, upload_to='companies', verbose_name='фото компании'),
        ),
    ]
