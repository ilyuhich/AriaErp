# Generated by Django 3.0.8 on 2020-07-30 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErpJobDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(db_index=True, max_length=30, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.AddField(
            model_name='erpjobname',
            name='dep_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='erp_system.ErpJobDepartment', verbose_name='Отдел'),
        ),
    ]
