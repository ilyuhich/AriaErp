from django.contrib import admin

# Register your models here.

from .models import ErpJobName
from .models import ErpJobDepartment
from .models import ErpEmployees
from .models import ErpJobType
from .models import ErpJob


class ErpJobNameAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'dep_name')


class ErpEmployeesAdmin(admin.ModelAdmin):
    list_display = ('emp_second_name', 'emp_name', 'emp_middle_name')


class ErpJobAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'job_addr', 'job_type')
    list_display_links = ('job_addr', '__str__')
    search_fields = ('pr_number', 'pr_type')


admin.site.register(ErpJobName, ErpJobNameAdmin)
admin.site.register(ErpJobDepartment)
admin.site.register(ErpEmployees, ErpEmployeesAdmin)
admin.site.register(ErpJob, ErpJobAdmin)
admin.site.register(ErpJobType)
