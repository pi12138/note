# URL的反向解析

	如果在视图、模板中使用硬编码的链接，在urlconf发生改变时，维护是一件非常麻烦的事情
	解决：在做链接时，通过指向urlconf的名称，动态生成链接地址
	视图：使用django.core.urlresolvers.reverse()函数
	模板：使用url模板标签

- 总结:
	- 在定义url时，需要为include定义namespace属性，为url定义name属性;
	- 使用时，在模板中使用url标签，在视图中使用reverse函数，根据正则表达式动态生成地址，减轻后期维护成本。

# 反向解析在视图中的使用
	
	```python
		from django.core.urlresolvers import reverse

		return redirect(reverse('namespace:name'))
	```

# 反向解析在模板中使用格式

	{% url 'namespace:name' value1 value2 %}

	namespace: 定义在项目目录下的urls.py文件中
	name: 定义在应用目录下的urls.py文件中
	value: 代表需要传入的参数

# 配置静态文件
	
	{% load static from staticfiles %}
	<img src='{% static "img/path.png" %}' />

# 反向解析的目的
	- 动态生成url，不需要硬编码，将来维护成本低

	

