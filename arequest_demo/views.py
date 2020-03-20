from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 1.1 使用正则
def login_one(request,addr,year):
    print("地址{0}".format(addr))
    print("年份{0}".format(year))

    return HttpResponse("路由传参")


# 1.2 使用注册器
def login_two(request,addr,year):
    print("地址{0}".format(addr))
    print("年份{0}".format(year))

    return HttpResponse("路由传参")


def login_three(request,year):
    print("年份{0}".format(year))
    return HttpResponse("自定义注册器捕获参数")

# 2.1 查询参数传参
def login_get(request):
    params = request.GET
    print(params)
    print(type(params))

    return HttpResponse("查询参数传参")

# 注册表单传参
def register_form(request):
    params = request.POST
    print(params)
    print(type(params))

    return HttpResponse("表单传参")

# 非注册表单传参
def register_not_form(request):
    params = request.body
    # 已字节的形式展示
    print(params.decode())
    print(type(params))

    return HttpResponse("非表单传参")

# 5.1表头传参
def login_header(request):
    params = request.META
    print(params['HTTP_A'])
    # 字典对象
    print(type(params)) 

    return HttpResponse("表头传参")

def index_one(request):

    return HttpResponse("index one")

def index(request):

    return HttpResponse("第一个子应用")