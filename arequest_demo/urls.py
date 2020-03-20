# -*- coding: utf-8 -*-
from django.urls import path

from . import views


urlpatterns = [
    path("index_one",views.index_one),
    path("index", views.index),
]
