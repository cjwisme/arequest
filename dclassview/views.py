from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

# 视图函数



class LoginView(View):
    def get(self,request):
        return HttpResponse("类视图----GET---登录页面")
    
    def post(self,request):
        return HttpResponse("类视图----POST---登录页面")


def index(request):
    if request.method == "GET":
        return HttpResponse("视图函数----GET---登录页面")
    elif request.method =="POST":
        return HttpResponse("视图函数----POST---登录页面")
