# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    # path("dclassview",views.index),

    # 类视图
    path("dclassview",views.LoginView.as_view()),
    path("dclassview_mixin",views.LoginViewMixin.as_view()),
]