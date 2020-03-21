from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View

# Create your views here.


# 装饰器

def login_decorator(func):
    def wrapper(self,request,*args,**kwargs):
        print("自定义装饰器")
        return func(self,request,*args,**kwargs)
    return wrapper

# 1.方式一 修改自定义装饰器

# 2.装饰在路由 path("dclassview",login_decorator(views.LoginView.as_view())),

# 3.调用django 自带的装饰方法 method_decorator()
def django_login_decorator(func):
    def wrapper(request,*args,**kwargs):
        print("自定义装饰器")
        return func(request,*args,**kwargs)
    return wrapper
#类视图
# @method_decorator(django_login_decorator,name="get")
@method_decorator(django_login_decorator,name="dispatch")
class LoginView(View):
    # @login_decorator
    @method_decorator(django_login_decorator)
    def get(self,request):
        return HttpResponse("类视图----GET---登录页面")
    
    def post(self,request):
        return HttpResponse("类视图----POST---登录页面")



# 视图函数
def index(request):
    if request.method == "GET":
        return HttpResponse("视图函数----GET---登录页面")
    elif request.method =="POST":
        return HttpResponse("视图函数----POST---登录页面")
