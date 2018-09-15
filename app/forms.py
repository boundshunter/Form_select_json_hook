#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

from app import models
from django import forms,
from django.forms import fields,widgets


class UserInfoForm(forms.Form):
    user = fields.CharField(
        required=False,
        widget=widgets.Textarea(attrs={'class': 'c1'})
    )

    pwd = fields.CharField(
        max_length=12,
        widget=widgets.PasswordInput(attrs={'class': 'c2'})
    )

    user_type =fields.ChoiceField(
        choices=[],
        widget=widgets.Select
    )

    user_type2 = fields.CharField(widget=widgets.Select(choices=[]))

    # 验证(*)
    # 生成HTML（保留上一次提交的数据)

    # 解URL方式操作(Form方式)
    # Ajax请求, 验证(*) 生成HTML  验证(*)


    def __init__(self, *args, **kwargs):
        super(UserInfoForm.self).__init__(*args, **kwargs)

        self.fields['user_type'].choices = models.UserType.objects.values_list('id','name')
        self.fields['user_type2'].widget.choices = models.UserType.objects.values_list('id', 'name')
