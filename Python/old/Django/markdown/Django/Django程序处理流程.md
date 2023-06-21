# `Django项目处理流程`

> - `nginx`作为接入层，通过其反向代理功能，监听80端口获取请求连接 -> 
> - 根据`nginx`配置，将请求交给后端服务器程序`wsgi server` ->
> - `wsgi server`调用执行`Django`的`wsgi.py`处理请求逻辑 -> 
> - `WSGIHandler`的`__call__`函数就是整个逻辑处理流程 -> 
> - 首先在`WSGIHandler ``__init__`中的加载中间件（中间件是一些列的类，这些类中有两大类函数，process_request和process_response，可以把它想象成一个装饰器，就是对request对象做处理，或者对response对象做处理） ->
> - 中间件处理request -> 
> - `urlpatterns`中指定的逻辑 -> 
> - 中间件处理response ->
> - 返回response



- `rest-framwork`就是上面流程中的`urlpatterns`指定的逻辑层，这个逻辑层对应的操作无非就是`http`协议定义的那几个方法，get，put，post，patch，delete等，`rest-framwork`所作的就是将这几个方法封装到特定的类里面，同时在这些类里面增加了一些其他的函数，比如请求方法判定，权限鉴定等操作，用户使用rest-framework的时候就可以继承rest-framework中定义好的某个或者某些类，当然rest-framework也给用户留了很多定制的空间，也可以理解，在使用rest-framework时，我们必须实现其中的部分功能。
  

