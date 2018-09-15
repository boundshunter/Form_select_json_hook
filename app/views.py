from django.shortcuts import render
from app import models
# Create your views here.


def ct(request):
    v = models.UserType.objects.create(name='普通用户')

    return render(request, 'ct.html', {'obj': v})