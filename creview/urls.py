# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    # cookie生成和获取
    path('response_cookie',views.response_cookie),
    path('get_cookie',views.get_request_cookie),
    # session 生成和获取
    path('response_session', views.response_session),
    path('get_request_session', views.get_request_session),
    path('del_request_session', views.del_session),
]