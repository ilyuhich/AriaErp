from django.contrib import admin

# Register your models here.

from .models import ErpJobName
from .models import ErpJobDepartment
from .models import ErpEmployees
from .models import ErpJobType
from .models import ErpJob


class ErpJobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'dep_name')


class ErpEmployeesAdmin(admin.ModelAdmin):
    list_display = ('emp_second_name', 'emp_name', 'emp_middle_name')


admin.site.register(ErpJobName, ErpJobAdmin)
admin.site.register(ErpJobDepartment)
admin.site.register(ErpEmployees, ErpEmployeesAdmin)
admin.site.register(ErpJob)
admin.site.register(ErpJobType)
