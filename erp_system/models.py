from django.db import models


# Create your models here.

class ErpJobName(models.Model):
    job_name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')
    dep_name = models.ForeignKey('ErpJobDepartment', null=True, on_delete=models.PROTECT, verbose_name='Отдел')

    def __str__(self):
        return self.job_name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['job_name']


class ErpJobDepartment(models.Model):
    dep_name = models.CharField(max_length=30, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return self.dep_name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class ErpEmployees(models.Model):
    emp_name = models.CharField(max_length=20, verbose_name='Имя')
    emp_middle_name = models.CharField(max_length=25, verbose_name='Отчество')
    emp_second_name = models.CharField(max_length=25, db_index=True, verbose_name='Фамилия')
    emp_phone = models.CharField(max_length=11)
    emp_job = models.ForeignKey('ErpJobName', null=True, on_delete=models.PROTECT, verbose_name='Должность')
    emp_dep = models.ForeignKey('ErpJobDepartment', null=True, on_delete=models.PROTECT, verbose_name='Отдел')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class ErpJobType(models.Model):
    job_type = models.CharField(max_length=20, verbose_name='Тип задания')

    def __str__(self):
        return self.job_type

    class Meta:
        verbose_name = 'Тип задания'
        verbose_name_plural = 'Типы заданий'


class ErpJob(models.Model):
    job_addr = models.CharField(max_length=100, verbose_name='Адрес')
    job_type = models.ForeignKey('ErpJobType', null=True, on_delete=models.PROTECT, verbose_name='Тип объекта')
    PR_TYPES = ((None, 'Выберите тип'),
                ('ПР', 'ПР'),
                ('НРД', 'НРД'),
                ('РТК', 'РТК'))
    pr_type = models.CharField(max_length=5, choices=PR_TYPES, default='НРД', verbose_name='Тип задания')
    pr_number = models.PositiveSmallIntegerField(max_length=6, verbose_name='Номер задания')
    pr_creation_date = models.DateTimeField(name='Дата создания', null=True)

    def __str__(self):
        return str(self.pr_type) + '-' + str(self.pr_number)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
