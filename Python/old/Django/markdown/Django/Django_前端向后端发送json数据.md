# 前端向后端传json数据

- 前后端分离的开发模式下，前端和后端进行数据交互，一般都是通过传递json数据来进行数据交互

## 前端如何给后端传递json数据

- 前端一般都可以通过ajax请求的方式给后端发送json数据
- 最近在使用ajax向后端传递数据时，遇到了一些问题，自己简单研究了一下，做个总结。
## 问题发现
- 起初我的ajax请求是这样写的
```javascript
        $("#error_data").click(function (){
            var url = "/show/test_json/";
            var data = {
                "list": [1,2],
                "name": "xxx",
                "text": "中国人"
            };

            $.ajax({
                url: url,
                data: data,
                type: "POST",
                contentType : "application/json",
                traditional: true,
                success: function(data) {
                    console.log(data);
                },
                error: function (data) {
                    console.log(data);
                }
            });
        });
```

- 然后我发现我在后端接受到的数据是这样的

```python
	print(request.POST)
    print(request.method)
    print(request.body)
```
```log
<QueryDict: {}>
POST
b'list=1&list=2&name=xxx&text=%E4%B8%AD%E5%9B%BD%E4%BA%BA'
```
- 当我准备给request.body解码后然后进行序列化，这个时候错误就发生了
```log
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

## 问题解决
- 在网上找了一些资料发现，问题原因在于，我没有对往后端传的数据，进行处理；
- 需要将json对象转换为json字符串，然后在向后端传递
```javascript
        $("#send_btn").click(function (){
            var url = "/show/test_json/";
            var data = {
                "list": [1,2],
                "name": "xxx",
                "text": "中国人"
            };

            $.ajax({
                url: url,
                data: JSON.stringify(data),
                type: "POST",
                contentType : "application/json",
                dataType: "text",
                traditional: true,
                success: function(data) {
                    console.log(data);
                    console.log(JSON.parse(data));

                },
                error: function (data) {
                    console.log(JSON.parse(data));
                }
            });

        });
```
- 后端接收到的数据
```log
<QueryDict: {}>
POST
b'{"list":[1,2],"name":"xxx","text":"\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba"}'
```
- 这样后端就可以对request.body内容解码后，进行序列化了。
## 问题总结
- 前端向后端传递json数据时，需要使用`JSON.stringify()`将json对象转化为json字符串。
- Django后端接收前端传递过来的json数据，不能使用`request.POST`而是要使用`request.body`
- `request.body`的数据为bytes类型，要想使用，需要先解码。

## ajax请求解决csrf_token验证的办法

- 发送请求时，添加参数`headers: {"X-CSRFtoken": $.cookie("csrftoken")},`
- 注意：使用`$.cookie("csrftoken")`获取cookie中的csrftoken值之前，需要先引入jQuery和jquery-cookie所需要的相关库文件。

## 发送json数据和表单数据在解决csrf_token问题的不同之处

- 发送json数据，需要在ajax的请求参数中添加参数`headers: {"X-CSRFtoken": $.cookie("csrftoken")}`
- 发送表单数据，需要在发送的数据data中添加键值对`"csrfmiddlewaretoken": token`