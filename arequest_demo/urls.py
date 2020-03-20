# -*- coding: utf-8 -*-
from django.urls import path, re_path,register_converter

from arequest_demo.converter import FourDigitYearConverter
from . import views

urlpatterns = [
    path("index_one", views.index_one),
    path("index", views.index),
]

# https://docs.djangoproject.com/en/3.0/topics/http/urls/#how-django-processes-a-request

register_converter(FourDigitYearConverter,'yyyy')
# 传参详解
urlpatterns += [
    # 1.1 路由传参  使用正则
    re_path(r"^login/(?P<year>\d{4})/(?P<addr>[a-z]+)$", views.login_one),
    # 1.2 使用注册器
    path("login/<int:year>/<str:addr>/",views.login_two),
    # 1.3 自定义注册器
    path("login/<yyyy:year>/", views.login_three),
    
    # 2.1 查询参数传参
    path("login", views.login_get),
    # 3.1 form 表单传参
    path("register_form",views.register_form),
    # 4.1 非表单传参
    path("register_not_form", views.register_not_form),
    
    # 5.1  表头传参
    path("login_header", views.login_header),

]
