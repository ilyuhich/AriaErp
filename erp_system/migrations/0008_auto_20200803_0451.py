# Generated by Django 3.0.8 on 2020-08-03 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_system', '0007_auto_20200803_0428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='erpjob',
            name='Дата создания',
        ),
        migrations.AddField(
            model_name='erpjob',
            name='pr_creation_date',
            field=models.DateTimeField(null=True, verbose_name='Дата создания'),
        ),
    ]
