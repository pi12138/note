# `Serializer`总结

## 序列化的作用

- 序列化数据(将“模型实例”转化为“Python原生数据类型”)
- 对用户请求传过来的数据进行验证

## 序列化的步骤

- 创建序列化类
- 编写序列化字段
- 获取需要序列化的数据（可以是前端传过来的数据，也可以是后端从数据库中取出来的数据）
- 对数据进行序列化
- 返回客户端展示或者服务器存储 

### 如何编写特殊序列化字段

- 当一个模型类中的一些字段和其他模型类有关联时（ForeignKey, ManyToManyField)，序列化后返回的数据可能不是我们想要的。
- 外键字段
    - 默认显示`__str__`方法的返回值
    - 如何想自定义显示，可以在定义字段时添加source参数，`source="FK_field.field"`，来获取我们想要的字段。
- 多对多字段
    - 显示关联对象的查询集
    - 通过手动编写，获取自己需要的数据
    - 可以使用`SerializerMethodField()`字段，来自定义一个方法获取自己需要的数据

## `Serializer和ModelSerializer`的区别

- Serializer的序列化字段完全需要自己编写
- ModelSerializer进行简单配置就可以自动生成需要的序列化字段，如果有需要也可以自定义序列化字段

- 如果需要保持前端传入的数据，继承Serializer类的序列化类，需要自己编写create()方法

## 自动序列化连表操作

- 当表与表之间有关联关系时，可以通过深度控制，来跟方便序列化关联表中的字段
- 继承ModelSerializer，设置 depth 字段

## 生成链接

- 有时要求返回的内容不是序列化后的ID，而是一个可以访问的链接
- 定义一个 

## 请求数据校验

### 对前端发送过来的数据，通过序列化类进行序列化

```python
ser = SerializerClass(data=frontend_data)
if ser.is_valid():
    print(ser.validated_data)
else:
    print(ser.errors)
```

- 通过 .is_valid() 进行判断数据是否有效
- 如果验证通过，合法的数据就会被保存在 `.validated_data` 属性中
- 如果数据校验不通过，序列化器把不符合要求的字段的错误信息给放在了 `.errors` 属性里

### 对后端从数据库中取出的数据进行校验

```python
test = TestModel.objects.get(field=data)
ser = SerializerClass(instance=test)
print(ser.data)
```

- 通过 .data 属性来访问验证之后的数据。
- 如果有多个实例

```python
tests = TestModel.objects.all()
ser = SerializerClass(instance=test, many=True)
print(ser.data)
```

- 此时 .data 属性变成了一个列表。