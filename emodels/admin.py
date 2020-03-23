from django.contrib import admin

# 创建超级管理员

# Register your models here.
from django import forms

from .models import HeroInfo, BookInfo


# https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin

class HeroInline(admin.TabularInline):
    model = HeroInfo
    # 设置几个多选框
    extra = 0
    verbose_name = '英雄'
    verbose_name_plural = verbose_name


# class HeroInline(admin.StackedInline):
#     model =  HeroInfo

class BookInfoForm(forms.ModelForm):
    class Meta:
        model = BookInfo
        exclude = ["is_delete"]


# 方式一
@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    # 列表列
    # column 展示的列名
    # list_display = [f.name for f in BookInfo()._meta.fields]
    # 设置那个字段跳转详情页
    # list_display_links = ['btitle']
    # list_display = ['btitle','bpub_date','bread','bcomment','is_delete']
    # list_per_page = 2
    # 默认根据list_display
    # sortable_by =  ["bpub_date","bread","bcomment"]
    # 搜索框
    # search_fields = ['btitle']
    # 显示 一行时间
    # date_hierarchy = 'bpub_date'

    # 修改和增加验证的表单，管理类定义了fields,fieldsets,form表单不需要定义 exclude 同理
    form = BookInfoForm

    # 外键的primarykey 时使用
    inlines = [
        HeroInline,
    ]

    # 详情页
    # save_on_top = True
    # 取消显示的字段
    # exclude = ["is_delete"]
    # 展示的字段 元组一行显示多个字段
    # fields = [("btitle","bpub_date"),"bread","bcomment"]
    #     # 分组
    # fieldsets = (
    #     ('必填',{
    #         'fields':['btitle','bpub_date'],
    #         'description':'<h1>图书的标题，和发布时间<h1>'
    #     }),
    #     ('选填',{
    #         'fields': ['bread', 'bcomment'],
    #         "classes":("collapse",)
    #     })
    # )


class HeroInfoForm(forms.ModelForm):
    class Meta:
        model = HeroInfo
        exclude = ['id']


# 方式二
class HeroInfoAdmin(admin.ModelAdmin):
    form = HeroInfoForm


admin.site.register(HeroInfo, HeroInfoAdmin)
