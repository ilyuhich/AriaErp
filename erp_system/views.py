from django.shortcuts import render

from .models import ErpJob


# Create your views here.


def index(request):
    jobs = ErpJob.objects.order_by()
    return render(request, 'erp_system/base.html', {'jobs': jobs})
