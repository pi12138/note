# 视图
- Django的视图函数，必须接受一个 HttpRequest 实例作为他的第一个参数，必须返回一个 HttpResponse实例。
- 视图接受web 请求(request) 并且返回web 响应(response)
- 视图就是一个python函数，被定义在 views.py 文件中
- 响应 可以是一张网页的 HTML 内容，一个重定向，一个404错误 ....
- 响应流程：
	1. 用户在浏览器中输入网址
		127.0.0.1:8000/booktest/index/
	2. django 获取地址信息，去除域名和端口部分，
		取余下 booktest/index/
	3. 将请求地址，按定义顺序逐个匹配，urlconf 的正则部分，一旦匹配成功则记录下来对应的 方法名称
	4. 调用找到的 方法 ，接受 request 及 正则表达式 中获取的值，处理并返回 response 对象

## HttpRequest 对象
- 服务器接受到 http 协议的请求后，会根据报文创建 HttpResquest 对象
- 视图函数的第一个参数就是 HttpResquest 对象
- 在 django.http 模块中定义了 HttpRequest 对象的API
	from django.http import HttpRequest

- 属性：(大部分属性都是 只读 的)
	- path:一个字符串，表示请求的页面的完整路径，不包含域名
	- method:一个字符串，表示请求使用的 HTTP 方法，常用值包括 "GET", "POST"
	- encoding:一个字符串，表示提交数据的编码方式
				属性可写
	- GET:一个类似于字典的对象，包含get请求方式的所有参数
	- POST:一个类似于字典的对象，包含post请求方式的所有参数
	- FILES:一个类似于字典的对象，包含所有 上传文件
	- COOKIES:一个标准的python字典，包含所有cookie，键和值都为字符串
	- session:一个类似于字典的对象，表示当前会话，只有当Django启用会话支持时才可用
				属性可读又可写
- 方法：
	- is_ajax(): 如果请求是通过XML HttpRequest 发起的，则返回True

## QueryDict 对象
- 定义在django.http.QueryDict
- "GET", "POST" 属性都是 QueryDict 类型的对象
- 与 python 字典不同，QueryDict 类型的对象用来处理同一个键带有多个值的情况

- 方法：
	- get():根据键获取值
		- 只能获取键的一个值
		- 如果一个键同时拥有多个值，获取最后一个值

		```
			dict.get("键", "设置默认值，如果键不存在返回默认值")
			或者写为
			dict['键']

			# 第二种写法，如果 键 不存在，会报错
		```
	- getlist():根据键获取值
		- 将键的值以列表形式返回，可用获取一个键的多个值
		```
			dict.getlist('键', default)
		```

## GET 属性
- QueryDict类型的对象
- 包含get请求方式的所有参数
- 与url请求地址中的参数对应，位于?后面
- 参数的格式是键值对，如key1=value1
- 多个参数之间，使用&连接，如key1=value1&key2=value2
- 键是开发人员定下来的，值是可变的

## POST 属性
- QueryDict类型的对象
- 包含post请求方式的所有参数
- 与form表单中的控件对应
- 问：表单中哪些控件会被提交？
  答：控件要有name属性，则name属性的值为键，value属性的值为键，构成键值对提交
- 对于checkbox控件，name属性一样为一组，当控件被选中后会被提交，存在一键多值的情况
- 键是开发人员定下来的，值是可变的

## 类视图

- Django中的视图分为两种 FBV（function base view , 基于函数的视图） 和 CBV（class base view ， 基于类的视图）

	- [类视图的简单使用](https://docs.djangoproject.com/en/1.8/topics/class-based-views/intro/)

```python
# views.py
from django.http import HttpResponse
from django.views.generic import View

class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')

# urls.py
from django.conf.urls import url
from myapp.views import MyView

urlpatterns = [
    url(r'^about/', MyView.as_view()),
]
```

- 本质：基于反射来实现
- 流程：路由 --> view --> dispatch(反射)
- 取消csrf认证，（装饰器要加到dispatch方法上，且method_decorator装饰）

## 输出非HTML内容

- 从一个视图返回一个非 HTML 内容的关键是在构造一个 `HttpResponse` 类时，需要指定 `content_type`(老版本使用`mimetype`) 参数。 通过改变 MIME 类型，我们可以通知浏览器将要返回的数据是另一种类型。

  ```python
  def ret_image(request):
      """返回一张图片"""
      image = open('./media/timg.png', 'rb').read()
      return HttpResponse(image, content_type="image/png") 
  ```

