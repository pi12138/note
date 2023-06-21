# `Renderers 渲染器`

- REST框架包括许多内置的Renderer类，它们允许你使用各种媒体类型返回响应。还支持定义你自己的自定义渲染器，这样可以灵活地设计你自己的媒体类型。

## `JSONRenderer`

- 使用utf-8编码将请求的数据渲染成`JSON`。

## `BrowsableRenderer`

- 将数据渲染成可视化的API，适当浏览器观看效果更佳。

### 修改drf官方logo

- 在BrowsableRenderer类渲染后的浏览器页面，默认在左上角有个drf的官方logo，以及官方文档链接
- 可以通过修改rest_framework默认的模板文件进行修改
- 默认模板文件位置：`rest_framework/api.html`
- `F:\python\virtualenv\Envs\django_rest2\Lib\site-packages\rest_framework\templates\rest_framework\base.html`

## `AdminRenderer`

- 将数据渲染给HTML以进行类似管理的显示：
- 此渲染器适用于CRUD风格的Web API，还应提供用于管理数据的用户友好界面。
- 请注意，包含嵌套或列表序列化器的输入视图对于`AdminRenderer`将无法正常工作，因为HTML表单无法正确支持它们。