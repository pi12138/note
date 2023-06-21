# `Throttling`节流

- 即，控制访问频率

- 问题：
  - 如何限制同一个用户在1分钟内访问的次数，比如一分钟最多访问3此
- 解决方法：
  - 将用户访问时间存储起来，进行比较

## 自定义节流使用

- 创建一个节流类，继承与BaseThrottle，并重写 allow_request() 方法

- 返回值：

  - True，允许该请求
  - False，拒绝该请求

- 还可以重写 wait() 方法，用于返回频繁操作后需要等待的时间

- 全局应用在settings中进行配置

- 局部应用在需要使用的视图类中进行配置`throttle_classes`字段

  ```python
  # -*- coding: utf-8 -*-
  from rest_framework import throttling
  import time
  
  
  IP_DICT = {}
  
  
  class MyThrottling(throttling.BaseThrottle):
      """
      自定义节流类，一分钟最多访问3次
      """
      def __init__(self):
          self.history = None
  
      def allow_request(self, request, view):
          # 1. 获取访问IP
          remote_addr = request.META.get('REMOTE_ADDR')
          ctime = time.time()
  
          if remote_addr not in IP_DICT:
              IP_DICT[remote_addr] = [ctime, ]
              return True
  
          history = IP_DICT.get(remote_addr)
          self.history = history
  
          while history and ctime - history[-1] > 60:
              history.pop()
  
          if len(history) >= 3:
              return False
  
          history.insert(0, ctime)
  
          return True
  
      def wait(self):
          """
          提示还需要等多少秒
          :return: 等待时间
          """
          ctime = time.time()
  
          return 60-(ctime-self.history[-1])
  ```

  



## `SimpleRateThrottle`

- 该类是继承之`BaseThrottle`类的一个子类

- 该类对节流需要的操作已经进行了部分实现，

- 如果继承该类需要设置一些字段即可实现节流，不用我们自己来实现节流的逻辑，较为方便

- 继承该类的节流类，需要设置字段`scope`，用来控制节流次数，

- 实现`get_cache_key()`方法，通过返回不同的值，来控制通过什么方式来进行节流（例如：通过IP或通过用户名）

  ```python
  class IPThrottling(throttling.SimpleRateThrottle):
      scope = "ip_throttling"
  
      def get_cache_key(self, request, view):
          # 返回IP地址
          return self.get_ident(request)
  
  
  class UserThrottling(throttling.SimpleRateThrottle):
      scope = 'user_throttling'
  
      def get_cache_key(self, request, view):
          # 返回用户名
          return request.user.username
  ```

- 编写完节流类后需要在settings文件中进行响应的配置

  ```python
  REST_FRAMEWORK = {
     	# 设置全局节流类，也可以在视图中进行局部设置
      'DEFAULT_THROTTLE_CLASSES': [
          # 'auth.throttling.IPThrottling',
          'auth.throttling.UserThrottling',
      ],
      # 通过 scope 参数进行控制节流次数 
      'DEFAULT_THROTTLE_RATES': {
          'ip_throttling': '3/m',
          'user_throttling': '10/m',
      }
  }
  ```

  