# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path("login_res",views.login_res),
    path("login_attr_res",views.login_attr_res),
    path("login_json",views.login_json),
]
