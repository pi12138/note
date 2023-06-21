# `APIView`

- 继承 django 原生的视图view

- APIView和View的不同点
  - 被传入到处理方法的请求不会是Django的`HttpRequest`类的实例，而是REST framework的`Request`类的实例。
  - 处理方法可以返回REST framework的`Response`，而不是Django的`HttpRequest`。视图会管理内容协议，给响应设置正确的渲染器。
  - 任何`APIException`异常都会被捕获，并且传递给合适的响应。
  - 进入的请求将会经过认证，合适的权限和（或）节流检查会在请求被派发到处理方法之前运行。
- 相同点
  - 使用`APIView`类和使用一般的`View`类非常相似，通常，进入的请求会被分发到合适处理方法比如`.get()`，或者`.post`。另外，很多属性会被设定在控制API策略的各种切面的类上。

## `GenericAPIView`

- 继承自 APIView
- 该类不常用