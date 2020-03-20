from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.

# 方式一
def login_res(request):
    return HttpResponse(
        content="响应参数",
        content_type='text/html',  # 默认
        status=200,
    )


def login_attr_res(request):
    response = HttpResponse()
    response.content = "属性形式传参"
    response.status_code = 200
    return response


def login_json(request):
    # data = {
    #     "a":20,
    #     "c":10,
    #     "a":30,
    # }
    data = [
        {
            "a": 20,
            "c": 10,
            "a": 30,
        }
    ]
    return JsonResponse(data,safe=False)
