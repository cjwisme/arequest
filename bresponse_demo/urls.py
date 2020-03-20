# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path("login_res",views.login_res,name="redirect_url"),
    path("login_attr_res",views.login_attr_res),
    path("login_json",views.login_json),
]

# 重定向
urlpatterns += [
    path("login_redirect",views.login_redirect),
    path("login_redirect_reverse",views.login_redirect_reverse),
]