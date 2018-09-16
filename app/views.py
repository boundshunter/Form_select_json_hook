from django.shortcuts import render, HttpResponse
from app import models
from app.forms import UserInfoForm
# Create your views here.

#
# def ct(request):
#     v = models.UserType.objects.create(name='普通用户')
#
#     return render(request, 'ct.html', {'obj': v})


def index(request):
    obj = UserInfoForm()  # 获取form对象
    # obj.fields['user_type'].choices = models.UserType.objects.values_list('id', 'type_name')
    # print(models.UserType.objects.values_list('id', 'type_name'))
    return render(request, 'index.html', {'obj': obj})


def test(request):
    v = models.UserType.objects.values_list('id', 'type')

    return HttpResponse(v)