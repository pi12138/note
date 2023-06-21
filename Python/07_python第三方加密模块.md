# python第三方加密模块

## itsdangerous

- 安装：`pip install itsdangerous`
- 简单使用：

```python
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# 创建一个对象
# 第一个参数为加密密钥，第二个参数为过期时间，单位为秒
serializer = Serializer("jiamimiyao", 60)

info = {"info": "jiami"}

# 使用 dumps() 进行加密，返回结果为一个bytes类型数据
result = serializer.dumps(info)

print(result)	
# b'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU1NjM0NzE5OCwiZXhwIjoxNTU2MzQ3MjU4fQ.eyJpbmZvIjoiamlhbWkifQ.GgkY-LDWSobfRVRMqEXPVZTgkqrMNzwJOCbIkK2wFDY-FEzFmsxOKIHUlZxPEG2sgTRE0S5lZuinE6mHA4kaaA'

# 使用 loads() 进行解密
jm = serializer.loads(result)
print(jm)	# {'info': 'jiami'}	
```
