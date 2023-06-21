# `Versioning 版本`

- django rest framework 2.0 版本中没有这个组件

## 自定义版本类

- url 中通过GET方式传参
- 自定义的版本类需要继承 BaseVersioning 类，并且实现 datarmine_version() 方法
- 局部使用，需要使用的视图类添加 versioning_class 字段

## 内置版本类

### `QueryParameterVersioning`

- 此方案是一种在 URL 中包含版本信息作为查询参数的简单方案

  ```text
  GET /something/?version=0.1 HTTP/1.1
  Host: example.com
  Accept: application/json
  ```

  

### `URLPathVersioning`

- 此方案要求客户端将版本指定为URL路径的一部分。

  ```text
  GET /v1/bookings/ HTTP/1.1
  Host: example.com
  Accept: application/json
  ```

- 你的URL conf中必须包含一个使用`'version'`关键字参数的匹配模式，，以便版本控制方案可以使用此版本信息。

  ```python
  urlpatterns = [
      url(
          r'^(?P<version>(v1|v2))/bookings/$',
          bookings_list,
          name='bookings-list'
      ),
      url(
          r'^(?P<version>(v1|v2))/bookings/(?P<pk>[0-9]+)/$',
          bookings_detail,
          name='bookings-detail'
      )
  ]
  ```

  

  