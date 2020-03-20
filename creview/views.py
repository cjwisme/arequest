from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def response_cookie(request):
    response = HttpResponse()
    response.content = "响应cookie"
    response.set_cookie("name","cjw")
    return response

def get_request_cookie(request):
    cookies = request.COOKIES
    print(cookies)
    response = HttpResponse()
    response.content = "获取cookie"
    return response


def response_session(request):
    request.session["name"] = "cjw"
    response = HttpResponse()
    response.content = "响应session"
    return response

def get_request_session(request):
    print(request.session['name'])
    response = HttpResponse()
    response.content = "获取响应session"
    return response

def del_session(request):
    # 1.del 删除指定的值
    # del request.session["name"]
    # 2.clear 清空所有session 值
    # request.session.clear()
    # 3.flush 删除整条记录
    request.session.flush()
    response = HttpResponse()
    response.content = "删除响应session"
    return response