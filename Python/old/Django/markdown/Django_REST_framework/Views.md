# `	Views（视图）`

## `Class Based Views(基于类的视图)`

- REST框架提供了一个`APIView`类，它是Django `View`类的子类。

- `APIView`类`View`通过以下方式与常规类不同：
  - 传递给处理程序方法的请求将是REST框架的`Request`实例，而不是Django的`HttpRequest`实例。
  - 处理程序方法可以返回REST框架`Response`，而不是Django `HttpResponse`。该视图将管理内容协商并在响应上设置正确的渲染器。
  - 任何`APIException`例外都将被捕获并调解为适当的响应。
  - 将对传入的请求进行身份验证，并在将请求分派给处理程序方法之前运行适当的权限和/或限制检查。

- 使用`APIView`该类与使用常规`View`类几乎相同，像往常一样，传入的请求被分派到适当的处理程序方法，如`.get()`或`.post()`。另外，可以在控制API策略的各个方面的类上设置许多属性。

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
```

- 属性
  - renderer_classes
  - parser_classes
  - authentication_classes
  - throttle_classes
  - permission_classes
  - content_negotiation_class
- 方法
  - get_renderers(self)
  - get_parsers(self)
  - get_authenticators(self)
  - get_throttles(self)
  - get_permissions(self)
  - get_content_negotiation(self)



## `Function Based Views(基于函数的视图)`

- REST框架还允许您使用基于常规功能的视图。它提供了一组简单的装饰器，它们包装基于函数的视图，以确保它们接收一个实例`Request`（而不是通常的Django `HttpRequest`），并允许它们返回一个`Response`（而不是Django `HttpResponse`），并允许您配置请求的处理方式。

- `@api_view(http_method_names)`

```python
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})
```



## `Generic views(通用视图)`

- 基于类的视图（CBV）的一个主要好处是它们允许您组合可重用行为的方式。REST框架通过提供许多提供常用模式的预构建视图来利用这一点。

- REST框架提供的通用视图（Generic views）允许您快速构建与您的数据库模型紧密相关的API视图。

- 如果通用视图（Generic views）不适合您的API需求，您可以直接使用常规`APIView`类，或者重用通用视图使用的mixins和基类来组成您自己的可重用通用视图集。

- 通常，在使用通用视图时，您将覆盖视图，并设置多个类属性。

  ```python
  from django.contrib.auth.models import User
  from myapp.serializers import UserSerializer
  from rest_framework import generics
  from rest_framework.permissions import IsAdminUser
  
  class UserList(generics.ListCreateAPIView):
      queryset = User.objects.all()
      serializer_class = UserSerializer
      permission_classes = (IsAdminUser,)
      paginate_by = 100
  ```

  

- 对于更复杂的情况，您可能还希望覆盖视图类上的各种方法。例如。

  ```python
  class UserList(generics.ListCreateAPIView):
      queryset = User.objects.all()
      serializer_class = UserSerializer
      permission_classes = (IsAdminUser,)
  
      def get_paginate_by(self):
          """
          Use smaller pagination for HTML representations.
          """
          if self.request.accepted_renderer.format == 'html':
              return 20
          return 100
  
      def list(self, request):
          # Note the use of `get_queryset()` instead of `self.queryset`
          queryset = self.get_queryset()
          serializer = UserSerializer(queryset, many=True)
          return Response(serializer.data)
  ```



## `GenericAPIView`

- 此类扩展了REST框架的`APIView`类，为标准列表和详细信息视图添加了常用的行为。提供的每个具体通用视图是通过`GenericAPIView`与一个或多个mixin类组合而构建的。

- 属性

  - `queryset` - 应该用于从此视图返回对象的查询集。通常，您必须设置此属性，或覆盖该`get_queryset()`方法。如果要覆盖视图方法，则调用`get_queryset()`而不是直接访问此属性非常重要，因为`queryset`将进行一次评估，并且将为所有后续请求缓存这些结果。
  - `serializer_class` - 应该用于验证和反序列化输入以及序列化输出的序列化程序类。通常，您必须设置此属性，或覆盖该`get_serializer_class()`方法。
  - `lookup_field` - 应该用于执行单个模型实例的对象查找的模型字段。默认为`'pk'`。请注意，使用超链接的API时，您需要确保*双方*的API意见*和*串行类设置查找字段，如果你需要使用一个自定义值。
  - `lookup_url_kwarg` - 应该用于对象查找的URL关键字参数。URL conf应包含与此值对应的关键字参数。如果未设置，则默认使用与...相同的值`lookup_field`。

- 方法

  - #### `get_queryset(self)`

    返回应该用于列表视图的查询集，该查询集应该用作详细视图中查找的基础。默认为返回`queryset`属性指定的查询集，如果`model`正在使用快捷方式，则返回模型的默认查询集。

    应始终使用此方法而不是`self.queryset`直接访问，因为`self.queryset`只进行一次评估，并为所有后续请求缓存这些结果。

    可以重写以提供动态行为，例如返回查询集，该查询集特定于发出请求的用户。

  - #### `get_object(self)`

    返回应该用于详细视图的对象实例。默认使用`lookup_field`参数来过滤基本查询集。

    可以重写以提供更复杂的行为，例如基于多个URL kwarg的对象查找。



## `Mixins`

- mixin类提供用于提供基本视图行为的操作。请注意，mixin类提供了操作方法，而不是直接定义处理程序方法，例如`.get()`和`.post()`。这允许更灵活的行为组合。
- ListModelMixin
- CreateModelMixin
- RetrieveModelMixin
- UpdateModelMixin
- DestoryModelMixin



## `Concrete View Classes(具体视图类)`

- 以下类是具体的通用视图。如果您使用的是通用视图，这通常是您将要工作的级别，除非您需要大量自定义的行为。
- CreateAPIView
- ListAPIView
- RetrieveAPIView
- DestroyAPIView
- UpdateAPIView
- ListCreateAPIView
- RetrieveUpdateAPIView
- RetrieveDestroyAPIView
- RetrieveUpdateDestroyAPIView



## `ViewSets(视图集)`

- Django REST framework允许你将一组相关视图的逻辑组合在单个类（称为 `ViewSet`）中。 在其他框架中，你也可以找到概念上类似于 'Resources' 或 'Controllers'的类似实现。

  `ViewSet` 只是**一种基于类的视图，它不提供任何方法处理程序**（如 `.get()`或`.post()`）,而是提供诸如 `.list()` 和 `.create()` 之类的操作。

  `ViewSet` 的方法处理程序仅使用 `.as_view()` 方法绑定到完成视图的相应操作。

  通常不是在 urlconf 中的视图集中显示注册视图，而是要使用路由类注册视图集，该类会自动为你确定 urlconf。

- 让我们定义一个简单的视图集，可用于列出或检索系统中的所有用户。

  ```python
  from django.contrib.auth.models import User
  from django.shortcuts import get_object_or_404
  from myapps.serializers import UserSerializer
  from rest_framework import viewsets
  from rest_framework.response import Response
  
  class UserViewSet(viewsets.ViewSet):
      """
      A simple ViewSet that for listing or retrieving users.
      """
      def list(self, request):
          queryset = User.objects.all()
          serializer = UserSerializer(queryset, many=True)
          return Response(serializer.data)
  
      def retrieve(self, request, pk=None):
          queryset = User.objects.all()
          user = get_object_or_404(queryset, pk=pk)
          serializer = UserSerializer(user)
          return Response(serializer.data)
  ```

- 如果需要，我们可以将此视图集绑定到两个单独的视图中，如下所示：

  ```python
  user_list = UserViewSet.as_view({'get': 'list'})
  user_detail = UserViewSet.as_view({'get': 'retrieve'})
  ```

- 通常我们不会这样做，而是使用路由器注册视图集，并允许自动生成urlconf。

  ```python
  from myapp.views import UserViewSet
  from rest_framework.routers import DefaultRouter
  
  router = DefaultRouter()
  router.register(r'users', UserViewSet)
  urlpatterns = router.urls
  ```

- 您通常希望使用提供默认行为集的现有基类，而不是编写自己的视图集。例如：

  ```python
  class UserViewSet(viewsets.ModelViewSet):
      """
      A viewset for viewing and editing user instances.
      """
      serializer_class = UserSerializer
      queryset = User.objects.all()
  ```

- 与使用 `View` 类相比，使用 `ViewSet` 类有两个主要优点。

  - 重复的逻辑可以组合成一个类。在上面的例子中，我们只需要指定一次 `queryset`，它将在多个视图中使用。
  - 通过使用 routers, 哦们不再需要自己处理URLconf。

- 这两者都有一个权衡。使用常规的 views 和 URL confs 更明确也能够为你提供更多的控制。ViewSets有助于快速启动和运行，或者当你有大型的API，并且希望在整个过程中执行一致的 URL 配置。