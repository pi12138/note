# 分页使用

- [参考内容](https://www.cnblogs.com/wdliu/p/9142832.html)

## django-rest-framework提供的分页组件

- PageNumberPagination
- LimitOffsetPagination
- CursorPagination

## 简单使用

- 使用drf提供的分页组件

```Python
class AnnouncementViewSet(ViewSet):
    def list(self, request):
        query_set = Announcement.objects.all()

        page_obj = PageNumberPagination()
        page_res = page_obj.paginate_queryset(queryset=query_set, request=request, view=self)
        ser = AnnouncementSerializer(instance=page_res, many=True)

        return Response(ser.data)
```

- 基本流程
    1. 实例化分页类`page_obj = PageNumberPagination()`
    2. 获取分页数据`page_res = page_obj.paginate_queryset(queryset=query_set, request=request, view=self)`
    3. 序列化分页后的数据

## 自定义分页组件

```Python
class CustomPagination(PageNumberPagination)
    """自定义分页"""    
    page_size = 10              # 默认每页显示数据条数
    page_query_param = 'page'   # 分页关键参数即 `?page=2`
```

## 使用自定义分页

```Python
def list(self, request):
    """
    公告列表
    """
    query_set = Announcement.objects.all()

    page_obj = CustomPageiantion()
    page_res = page_obj.paginate_queryset(queryset=query_set, request=request, view=self)
    ser = AnnouncementSerializer(instance=page_res, many=True)

    return page_obj.get_paginated_response(ser.data)
```

- return 返回时使用 分页类提供的response函数, 返回内容, 具有上一页,下一页功能
- return 使用默认Response时, 返回数据为分页好的数据, 没有上一页下一页参数 