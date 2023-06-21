# `Routers（路由）`

- REST框架增加了对Django自动URL路由的支持，并为您提供了一种简单，快速和一致的方法，将您的视图逻辑连接到一组URL。

  ```python
  from rest_framework import routers
  
  router = routers.SimpleRouter()
  router.register(r'users', UserViewSet)
  router.register(r'accounts', AccountViewSet)
  urlpatterns = router.urls
  ```

  

>- 使用流程
>
>1. 创建一个路由对象
>2. 对视图进行注册
>3. urlpatterns

- `register(prefix, viewset)`参数
  - prefix -- 用于此路由的url前缀
  - viewset -- 视图集类

## `@detail_route和@list_route`

- 在视图集中被`@detail_route或@list_route`装饰的方法都将被路由。

