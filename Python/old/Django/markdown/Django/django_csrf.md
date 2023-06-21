# csrf
	- Cross Site Request Forgery, 跨站请求伪造


# 防csrf的使用
	- 在django中提供了防止跨站攻击的方法，步骤如下
	- step1：在settings.py 文件中启用"django.	middleware.csrf.CsrfViewMiddleware"中间件,此项在创建项目时背默认启用
	- step2：在<form>表单中添加DTL标签
		<form>
			{% csrf_token %}
		</form>
## csrf的使用

- 基于中间件的 process_view 方法

- 装饰器给单独函数进行设置（需要csrf认证`@csrf_protect`或者无需csrf认证`@csrf_exempt`）

- 全局：中间件 django.middleware.csrf.CsrfViewMiddleware

- 局部：

  - @csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置全局中间件。

  - @csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。

