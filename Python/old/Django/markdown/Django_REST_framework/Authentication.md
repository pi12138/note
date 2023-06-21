# `Authentication(认证)`

- 问题：
  - 有些API需要用户登录成功之后，才能访问；有些无需登录就能访问
- 解决：
  - 创建两张表（一张用户表，一张存用户的token信息）
  - 用户登录成功后，返回token并保存到数据库

## 如何实现认证

> - 编写一个专门的认证类，在该认证类中编写 authenticate() 方法
> - 在需要认证的视图类中加入`authentication_classes = [Auth_class, ]`

- 认证类要继承`authentication.BaseAuthentication`类，并且覆盖`authenticate()`方法
- 认证成功返回一个元组(user, auth)，认证失败返回(AnonymouseUser, None)
- 认证失败可以抛出异常，`raise exceptions.AuthenticationFailed("error msg")`

## 认证原理

1. 首先执行dispatch方法
2. 重新封装Request
3. initial(request)方法里面有各种封装函数
4. 其中perform_authentication(request)是认证的函数
5. 返回一个request.user
6. def _authenticate():循环所有的authentication对象，执行authenticate方法
7. Authtication 自定义认证类
   - def authenticate():
   - 自定义认证
     -  -报错
     -  -返回元组(request.user, request.auth)

- ![认证流程](../image/1.png)

## 认证的局部使用和全局使用

- 局部使用就是在需要认证的视图类中添加`authentication_classes`属性

- 全局使用需要在settings文件中进行配置， 配置认证类所在路径

  ```python
  # 局部使用
  from rest_framework.views import APIView
  class UserInfoView(APIView):
      authentication_classes = []
      def get(self, request, *args, **kwargs):
          print(request.user)
          return HttpResponse('用户相关信息')
  ```

  ```python
  # 全局使用
  REST_FRAMEWORK = {
      # 'DEFAULT_AUTHENTICATION_CLASSES': ['apps.api.utils.auth.FirstAuthtication', 'apps.api.utils.auth.Authtication'],
      # 全局使用的认证类
      'DEFAULT_AUTHENTICATION_CLASSES': ['apps.api.utils.auth.Authtication'],
      # 匿名用户相关内容
      'UNAUTHENTICATED_USER': None,
      'UNAUTHENTICATED_TOKEN': None,
  }
  ```

- 当设置全局认证后，当某个视图类不需要认证时，可以添加`authentications_classes = []`

## 内置认证类

- `rest_framework.Authentication`
  - `BaseAuthentication`
  - `BasicAuthentication`
  - `TokenAuthentication`

## 使用认证总结

- 创建一个自定义认证类，继承自`BaseAuthentication`， 并且要实现`authenticate`方法
- 返回值：
  - None，下一个认证继续执行。
  - raise exceptions.AuthenticationFailed('error msg')
  - (user, auth) ，user会赋值给request.user，auth会赋值给request.auth
- 全局使用和局部使用
  - settings文件进行配置
  - 单个视图类中添加`authentication_classes`字段

