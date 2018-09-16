#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

from app import models
from django import forms
from django.forms import fields, widgets, ModelChoiceField, ModelMultipleChoiceField


class UserInfoForm(forms.Form):
    user = fields.CharField(
        required=False,
        widget=widgets.Textarea(attrs={'class': 'c1'})
    )
    pwd = fields.CharField(
        max_length=12,
        widget=widgets.PasswordInput(attrs={'class': 'c2'})
    )
    user_type = fields.ChoiceField(
        # choices=[(1, '普通'), (2, '超级'), (3, '访客')],
        # choices=models.UserType.objects.values_list('id', 'type_name'),
        choices=[],
        widget=widgets.Select
    )
    # user_type2 = fields.CharField(widget=widgets.Select(choices=[(1, '普通用户'), (2, '超级用户'), ]))
    user_type2 = fields.CharField(widget=widgets.Select(choices=[]))
    # 验证(*)
    # 生成HTML（保留上一次提交的数据)
    # 解URL方式操作(Form方式)
    # Ajax请求, 验证(*) 生成HTML  验证(*)
    # def __init__(self, *args, **kwargs):
    #     super(UserInfoForm.self).__init__(*args, **kwargs)
    #     self.fields['user_type'].choices = models.UserType.objects.values_list('id','name')
    #     self.fields['user_type2'].widget.choices = models.UserType.objects.values_list('id', 'name')
    user_type3 = ModelChoiceField(
        queryset=models.UserType.objects.all(),
        empty_label="请选择用户类型",
        to_field_name='id',
    )
    user_type4 = ModelMultipleChoiceField(
        queryset=models.UserType.objects.all(),
    )

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__()
        self.fields['user_type'].choices = models.UserType.objects.values_list('id', 'type_name')
        self.fields['user_type2'].widget.choices = models.UserType.objects.values_list('id', 'type_name')