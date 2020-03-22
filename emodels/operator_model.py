# -*- coding: utf-8 -*-


from emodels.models import BookInfo,HeroInfo
from datetime import date

# 添加
# 1.方式一
BookInfo.objects.create(
    btitle="西游记",
    bpub_date=date(1995, 1, 1)
)
# 2.方式二
book = BookInfo(
    btitle="我不",
    bpub_date=date(1995, 1, 1)
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

# 查询操作
# get  filter  exclude all count
book = BookInfo.objects.get(id=1) #返回对象
book = BookInfo.objects.count()
book = BookInfo.objects.filter()
book = BookInfo.objects.all()
book = BookInfo.objects.exclude(id=1) #除之外

# 条件查询
# lt lte gt gte  exact
book = BookInfo.objects.filter(id__lte=3)

# 模糊查询
# contains startswith endswith
book = BookInfo.objects.filter(btitle__contains='龙')

# 日期查询
# year mouth day week
book = BookInfo.objects.filter(bpub_date__year=1995)
book = BookInfo.objects.filter(bpub_date__gte=date(1995))


# F和Q查询
from django.db.models import F,Q
book = BookInfo.objects.filter(bread__gt=F('bcomment'))

# and or not
book = BookInfo.objects.filter(Q(bread__gt=20),Q(id__lte=2))

# 聚合查询
from django.db.models import F,Avg,Sum,Max,Min
book = BookInfo.objects.aggregate(Avg("id"))

# 关联查询
# 1:n   obj.小写模型对象名_set.
book = BookInfo.objects.get(id=1)
# HeroInfo
heros = book.heroinfo_set.filter(hname__lt=2)

# n:1
hero = HeroInfo.objects.get(id=5)
book = hero.hbook

# 关联过滤查询
# n:1  格式  关联数据模型小写__属性名__条件=值
book = BookInfo.objects.filter(heroinfo__hname="乔峰")
# 1:n  格式    一模型关联的属性名__关联的模型属性名__条件=值
hero = HeroInfo.objects.filter(hbook__bread__gte=30)