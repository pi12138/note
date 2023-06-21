# `Serializer Fields(序列化字段)`

- Serializer Fields处理原始值和内部数据类型之间的转换。它们还处理验证输入值，以及从父对象检索和设置值。

- **注意：**序列化程序字段在fields.py中声明，但按照惯例，您应该使用它们导入它们`from rest_framework import serializers`并将字段引用为`serializers.<FieldName>`。

## 主要参数

- source

  - 将用于填充字段的属性的名称。可以是一个只接受`self`参数的方法，例如`Field(source='get_absolute_url')`，或者可以**使用点（.）**表示来遍历属性，例如`Field(source='user.email')`。

  - 当多表关联时，可以使用 点（.）来取得关联表的属性， 如下面的`group.group_name`。

    ```python
    # models.py
    class UserInfo(models.Model):
        user_type_choices = (
            (1, '普通用户'),
            (2, "VIP"),
            (3, "SVIP"),
        )
    
        username = models.CharField(max_length=32, unique=True)
        password = models.CharField(max_length=64)
        user_type = models.IntegerField(choices=user_type_choices)
        group = models.ForeignKey("GroupInfo")
        
    class GroupInfo(models.Model):
        """
        分组类
        """
        group_name = models.CharField(max_length=32, unique=True)
    ```

    ```python
    # serializer.py
    class UserInfoSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()
        user_type = serializers.CharField(source='get_user_type_display')
        group = serializers.CharField(source='group.group_name')
    ```

    

  - 该值`source='*'`具有特殊含义，用于指示整个对象应该传递到该字段。这对于创建嵌套表示非常有用。（有关`PaginationSerializer`示例，请参阅类的实现。）

  - 默认为字段的名称。

- read_only

  - 将其设置`True`为确保在序列化表示时使用该字段，但在反序列化期间创建或更新实例时不使用该字段。
  - 默认为 `False`

- write_only

  - 将其设置`True`为确保在更新或创建实例时可以使用该字段，但在序列化表示时不包括该字段。

  - 默认为 `False`

- required

  - 通常，如果在反序列化期间未提供字段，则会引发错误。如果在反序列化期间不需要此字段，则设置为false。
  - 默认为`True`。

- default

- validator

- error_messages

- label

- help_text

## 通用字段

- Field()

  - 通用的**只读**字段。您可以将此字段用于不需要支持写入操作的任何属性。

    ```python
    # models.py
    from django.db import models
    from django.utils.timezone import now
    
    class Account(models.Model):
        owner = models.ForeignKey('auth.user')
        name = models.CharField(max_length=100)
        created = models.DateTimeField(auto_now_add=True)
        payment_expiry = models.DateTimeField()
    
        def has_expired(self):
            return now() > self.payment_expiry
    ```

    ```python
    # serializers.py
    from rest_framework import serializers
    
    class AccountSerializer(serializers.HyperlinkedModelSerializer):
        expired = serializers.Field(source='has_expired')
    
        class Meta:
            model = Account
            fields = ('url', 'owner', 'name', 'expired')
    ```

  - 输出结果

    ```python
    {
        'url': 'http://example.com/api/accounts/3/',
        'owner': 'http://example.com/api/users/12/',
        'name': 'FooCorp business account',
        'expired': True
    }
    ```

    

- WritableField()
  
  - 一个支持读写操作的字段。它本身`WritableField`不会将输入值转换为给定类型。您通常不会直接使用此字段，但您可能希望覆盖它并实现`.to_native(self, value)`和`.from_native(self, value)`方法。
- ModelField()
  - 可以绑定到任意模型字段的通用字段。该`ModelField`级代表序列化/反序列化到其关联的模型领域的任务。此字段可用于为自定义模型字段创建序列化程序字段，而无需创建新的自定义序列化程序字段。
  - 该`ModelField`级一般用于内部使用，但如果需要的话可以通过您的API使用。为了正确实例化`ModelField`，必须传递一个附加到实例化模型的字段。例如：`ModelField(model_field=MyModel()._meta.get_field('custom_field'))`
  - **签名：** `ModelField(model_field=<Django ModelField instance>)`

- SerializerModelField()

  - 这是一个只读字段。它通过调用附加到的序列化程序类上的方法来获取其值。它可用于将任何类型的数据添加到对象的序列化表示中。字段的构造函数接受单个参数，该参数是要调用的序列化程序上的方法的名称。**该方法应该接受一个参数（除了`self`），这是被序列化的对象。它应该返回您想要包含在对象的序列化表示中的任何内容**。例如：

    ```python
    from django.contrib.auth.models import User
    from django.utils.timezone import now
    from rest_framework import serializers
    
    class UserSerializer(serializers.ModelSerializer):
        days_since_joined = serializers.SerializerMethodField('get_days_since_joined')
    
        class Meta:
            model = User
    
        def get_days_since_joined(self, obj):
            return (now() - obj.date_joined).days
    ```

    

## 类型字段

- 这些字段表示基本数据类型，并支持读取和写入值。

- BooleanField()
- CharField()
- URLField()
- SlugField()
- ChoiceField()
- EmailField()
- ......

- [Serializer field](http://www.tomchristie.com/rest-framework-2-docs/api-guide/fields)

  

## 自定义字段

- 创建自定义字段，需要自定义字段类继承`serializer.Field`，并且重写`.to_representation()`、`.to_internal_value()`方法中的一个或两个
- 调用 `.to_representation()` 方法将初始数据类型转换为原始的可序列化数据类型。
- 调用 `to_internal_value()` 方法将原始数据类型恢复为其内部 python 表示。如果数据无效，此方法应该引发 `serializers.ValidationError` 异常。

```python
class TEL(object):
    def __init__(self, num=None):
        self.num = num

    def text(self, message):
        return self._send_message(message)

    def _send_message(self, message):
        print("send {} to {}".format(message[:10], self.num))


class TELField(serializers.Field):
    def to_representation(self, tel_obj):
        return tel_obj.num

    def to_internal_value(self, data):
        data = data.lstrip().rstrip().strip()
        if 8 <= len(data) <= 11:
            return TEL(num=data)
        raise serializers.ValidationError("Invalid telephone number.")


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    tel = TELField()


frontend_data4 = {
    'name': 'xxx',
    'tel': 'xxxx123456'
}


con = ContactSerializer(data=frontend_data4)
if con.is_valid():
    print(con.validated_data)
    print(con.validated_data['tel'].num)

```

