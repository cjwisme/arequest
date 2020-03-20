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
