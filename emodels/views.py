from datetime import date
from django.shortcuts import render

# Create your views here.

def models_operator():
    from emodels.models import BookInfo
    # 添加
    # 1.方式一
    BookInfo.objects.create(
        btitle="西游记",
        bpub_date=date(1995,1,1)
    )
    # 2.方式二
    book = BookInfo(        
        btitle="我不",
        bpub_date=date(1995,1,1)
    )
    book.save()
    
    # 删除
    # 方式一
    book = BookInfo.objects.get(id=5)
    book.delete()
    # 方式二
    BookInfo.objects.filter(id=6).delete()
    
    # 更新
    # 方式一
    book = BookInfo.objects.get(id=4)
    book.bread = 30
    # 方式二
    BookInfo.objects.update(bread=30)