# `Django 会话`

## cookies

- 每一个 HttpRequest 对象都有一个 COOKIES 对象，该对象为一个字典。
- 读取cookies
  - request.COOKIES['key']
  - request.COOKIES.get(key)
- 写入cookies
  - 写入cookies，**需要使用** `HttpResponse`**对象的** `set_cookie(key, value)`**方法**

## session

- 每个传给视图(view)函数的第一个参数``HttpRequest`` 对象都有一个 `session` 属性，**这是一个字典型的对象**。 你可以象用普通字典一样来用它。

