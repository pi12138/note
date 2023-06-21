# Django REST framework

- `pip install djangorestframework`
- 

## settings

- 数据库 

  ```python
  DATABASES = {
      # 'default': {
      #     'ENGINE': 'django.db.backends.sqlite3',
      #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      # }
      'default': {
          "ENGINE": 'django.db.backends.mysql',
          "NAME": "mxshop",
          "USER": "root",
          "PASSWORD": "root",
          "HOST": "127.0.0.1",
          "OPTIONS": {"init_command": "SET storage_engine=INNODB"}
      }
  }
  ```


## `Django rest framework`生命周期

> - 前端发送请求-->
> - Django的wsgi-->
> - 中间件-->
> - 路由系统_执行CBV的as_view()，就是执行内部的dispath方法-->
> - 在执行dispath之前，有版本分析 和 渲染器-->
> - 在dispath内，对request封装-->版本-->认证-->权限-->限流-->
> - 视图-->如果视图用到缓存( request.data or   request.query_params )就用到了 解析器-->
> - 视图处理数据，用到了序列化(对数据进行序列化或验证) -->
> - 视图返回数据可以用到分页