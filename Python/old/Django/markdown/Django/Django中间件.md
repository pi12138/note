# Django中间件

- process_request
- process_view
- process_response
- process_exception
- process_template_response

## 使用中间件做什么？

- 权限
- 用户登录验证
- csrf token

## Django的csrf token 是如何实现的

- 使用@csrf_exempt装饰视图函数，可以使视图函数免除csrf验证 `(from django.views.decorators.csrf import csrf_exempt)`
- process_view方法检查视图是否被 @csrf_exempt 装饰
- 去请求体或cookie中获取token

- @csrf_protect 装饰视图函数，表示当前视图需要csrf验证(当取消了settings文件中的csrf中间件)

## process_request

- `process_request(self, request)`,Request的预处理函数，这个方法的调用在Django接收到 request 之后，但仍未解析URL以确定应当运行的view之前。 Django向它传入相应的 `HttpRequest` 对象，以便在方法中修改。

- `process_request()` 应当返回 `None` 或 `HttpResponse` 对象.

  - 如果返回 `None` , Django将继续处理这个request,执行后续的中间件， 然后调用相应的view.

  - 如果返回 `HttpResponse` 对象, Django 将不再执行 *任何* 其它的中间件(而无视其种类)以及相应的view。 Django将立即返回该 `HttpResponse` .

## process_view

- `process_view(self, request, view, *args, **kwargs) `，View预处理函数，这个方法的调用时机在Django执行完request预处理函数并确定待执行的view之后，但在view函数实际执行之前。

- 就像process_request（）一样，process_view（）应该返回None或HttpResponse对象

  - 如果它返回None，Django将继续处理此请求，执行任何其他中间件，然后执行相应的视图

  - 如果它返回一个HttpResponse对象，Django将不会打扰任何其他中间件（任何类型）或适当的视图。 Django将立即返回该HttpResponse。

## process_response

- `process_response(self, request, response) `这个方法的调用时机在Django执行view函数并生成response之后。这个方法的参数相当直观: `request` 是request对象，而 `response` 则是从view中返回的response对象。 

- 不同request和view预处理函数返回 `None` , `process_response()` *必须* 返回 `HttpResponse` 对象. 这个response对象可以是传入函数的那一个原始对象(通常已被修改)，也可以是全新生成的。