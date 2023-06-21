# `Template`

- 基本步骤：

  - 创建一个Template对象，加载模板数据

  - 创建一个Context对象，加载上下文数据
  - 使用模板对象的render(context_object)方法对模板进行渲染，该方法需要传入一个Context对象

  ```python
  >>> from django.template import Context, Template
  >>> t = Template("my name is {{name}}")
  >>> c = Context({'name': 'zyp'})
  >>> t.render(c)
  'my name is zyp'
  
  ```

  

## 在模板中比较两个变量的值

- `{% ifequal %}` 标签比较两个值，当他们相等时，显示在 `{% ifequal %}` 和 `{% endifequal %}` 之中所有的值。
-  `{% if %}` 类似， `{% ifequal %}` 支持可选的 `{% else%}` 标签