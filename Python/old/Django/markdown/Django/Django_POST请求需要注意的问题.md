# Django 中 POST 请求可能存在的问题

- 问题：

  - 有时明明提交了 POST 请求，却无法在 request.POST 中取到数据，这是为什么？

- 原因：

  1. 请求头要求：
     - Content-Type : application/x-www-form-urlencoded
  2. 数据格式要求：
     - name=zyp&age=20&gender=boy

  - 只有当提交的数据同时符合以上两种要求，POST请求提交数据才有内容

- 例如：

  - form 表单提交
  - ajax提交

- 例外：

  - ajax提交时可以定制请求头，当改变了Content-Type类型后，POST请求提交数据将在request.POST中无法取到。
  - ajax提交也可以改变提交数据的格式。

- 解决方法：

  - 当request.POST中无法取到值时，可以使用request.body
  
- 测试：

  - 使用Postman模拟POST请求，发送JSON格式数据；
  - 视图函数中分别使用request.POST和request.body接收数据；
  - 发现requets.POST中没有数据，request.body存在数据

  ![2](./image/2.png)

  ![3](./image/3.png)

  