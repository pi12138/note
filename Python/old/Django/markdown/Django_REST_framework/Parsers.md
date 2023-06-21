# `Parsers 解析器`

- 对请求体的数据进行解析
- django rest framework的解析器，比原生的django强大许多

- 一组视图的有效解析器总是被定义为一个类的列表（parsers_classes字段）。当访问`request.data`（`drf2.0 版本为 request.DATA`）时，REST框架将检查传入请求中的`Content-Type`头，并确定用于解析请求内容的解析器。

- 只有需要从 **请求体**（request.data) 里面取值时，解析器才会工作

  > **注意**: 开发客户端应用程序时应该始终记住在HTTP请求中发送数据时确保设置`Content-Type`头。
  >
  > 如果你不设置内容类型，大多数客户端将默认使用`'application/x-www-form-urlencoded'`，而这可能并不是你想要的。
  >
  > 举个例子，如果你使用jQuery的[.ajax() 方法](http://api.jquery.com/jQuery.ajax/)发送`json`编码数据，你应该确保包含`contentType：'application / json'`设置。

- 不同的数据需要使用不同的解析器，如果使用的解析器不符合要求，则会出现异常。

## drf自带解析器类

- JSONParser
  - 解析JSON请求内容
  - application/json
- YAMLParser
  - 解析YAML请求内容
  - application/yaml
  - 需要安装pyyaml
- XMLParser
- FormParser
- MultiPartParser
- FileUploadParser

## 解析器的使用

- 局部使用

  - 在需要使用的视图类中添加parsers_classes字段

- 全局使用

  - settings文件进行配置

    ```python
    REST_FRAMEWORK = {
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.YAMLParser',
        )
    }
    ```

    