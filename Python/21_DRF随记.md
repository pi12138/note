# DRF随记

## 1. 返回时间自动格式化

- drf 默认返回的时间样式是这样的 `2013-01-29T12:34:56.000000Z`, 可以通过指定参数 format 来改变显示的样式
- 格式化字符串可以是显式指定的 Python strftime 格式，也可以是表明使用 ISO 8601 样式的日期时间的特殊字符串
	- `create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)`