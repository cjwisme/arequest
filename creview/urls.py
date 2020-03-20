# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('response_cookie',views.response_cookie),
    path('get_cookie',views.get_request_cookie),
]