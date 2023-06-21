# `Serializers(序列化器)`

- 序列化器允许把像查询集和模型实例这样的复杂数据转换为可以轻松渲染成`JSON`，`XML`或其他内容类型的原生Python类型。序列化器还提供反序列化，在验证传入的数据之后允许解析数据转换回复杂类型。
- REST framework中的serializers与Django的`Form`和`ModelForm`类非常像。我们提供了一个`Serializer`类，它为你提供了强大的通用方法来控制响应的输出，以及一个`ModelSerializer`类，它为创建用于处理模型实例和查询集的序列化程序提供了有用的快捷实现方式。

## 如何使用序列化器

- 创建一个序列化类，该类继承drf提供的序列化类，

- 编写需要序列化的字段

  - 继承Serializer，需要手动编写序列化字段

  ```python
  class UserInfoSerializer(serializers.Serializer):
      username = serializers.CharField()
      password = serializers.CharField()
      user_type = serializers.CharField(source='get_user_type_display')
      # group = serializers.CharField(source='group.group_name')
  
  ```

  - ModelSerializer，可以通过简单配置来自动生成序列化字段，也可以手动配置

  ```python
  class UserInfoSerializer(serializers.ModelSerializer):
      group_info = serializers.SerializerMethodField('get_group')
      group = serializers.CharField(source='group.group_name')
      class Meta:
          model = UserInfo
          fields = ('username', 'password', 'user_type', 'group', 'group_info')
  
  ```

## 如何编写字段

- 按照序列化类的字段要求编写

  - 有些字段和其他表可能有关联，可以使用 点（.）取得

    ```python
    group = serializers.CharField(source='group.group_name')
    ```

    - **有时需要取得的字段内容比较复杂**，可以使用 SerializerMethodField() 定义字段，然后编写一个自定义的方法。

    ```python
    class UserInfoSerializer(serializers.ModelSerializer):
        # 自定义显示
        group_info = serializers.SerializerMethodField('get_group')
        class Meta:
            model = UserInfo
            fields = ('username', 'password', 'user_type', 'group', 'group_info')
    	
        # 自定义方法
        def get_group(self, obj):
            """
            自定义取字段的方法
            :param obj: 对应的模型类对象，这里时UserInfo类
            :return: 取到的具体数据
            """
            return [obj.group.group_name, obj.group.id]
    
    ```

    

## 声明序列化程序

- 让我们首先创建一个我们可以用于示例目的的简单对象：

  ```python
  class Comment(object):
      def __init__(self, email, content, created=None):
          self.email = email
          self.content = content
          self.created = created or datetime.datetime.now()
  
  comment = Comment(email='leila@example.com', content='foo bar')
  ```

- 我们将声明一个序列化器，我们可以使用它来序列化和反序列化`Comment`对象。声明序列化程序看起来与声明表单非常相似：

  ```python
  from rest_framework import serializers
  
  class CommentSerializer(serializers.Serializer):
      email = serializers.EmailField()
      content = serializers.CharField(max_length=200)
      created = serializers.DateTimeField()
  
      def restore_object(self, attrs, instance=None):
          """
          Given a dictionary of deserialized field values, either update
          an existing model instance, or create a new model instance.
          """
          if instance is not None:
              instance.email = attrs.get('email', instance.email)
              instance.content = attrs.get('content', instance.content)
              instance.created = attrs.get('created', instance.created)
              return instance
          return Comment(**attrs)
  ```

- serializer类的第一部分定义了序列化/反序列化的字段。该`restore_object`方法定义了在反序列化数据时如何创建完全成熟的实例。

- 该`restore_object`方法是可选的，只有在我们希望序列化程序支持反序列化为完全成熟的对象实例时才需要。如果我们不定义此方法，则反序列化数据将只返回项目字典。

## 序列化对象

- 我们现在可以`CommentSerializer`用来序列化评论或评论列表。同样，使用`Serializer`该类看起来很像使用`Form`类。

  ```python
  serializer = CommentSerializer(comment)
  serializer.data
  # {'email': u'leila@example.com', 'content': u'foo bar', 'created': datetime.datetime(2012, 8, 22, 16, 20, 9, 822774)}
  ```

- 此时我们已将模型实例转换为Python本机数据类型。为了完成序列化过程，我们将数据渲染到`json`。

  ```python
  from rest_framework.renderers import JSONRenderer
  
  json = JSONRenderer().render(serializer.data)
  json
  # '{"email": "leila@example.com", "content": "foo bar", "created": "2012-08-22T16:20:09.822"}'
  ```

  

## `ModelSerializer`

- 通常，您会希望序列化程序类与模型定义紧密相关。`ModelSerializer`类可以自动创建一个序列化器类与对应型号字段的字段。

- **这个ModelSerializer类和常规的Serializer类一样，不同的是**：

  - 它根据模型自动生成一组字段。
  - 它自动生成序列化器的验证器，比如unique_together验证器。
  - 它默认简单实现了`.create()`方法和`.update()`方法。

- 声明一个`ModelSerializer`如下：

  ```python
  class AccountSerializer(serializers.ModelSerializer):
      class Meta:
          model = Account
          fields = ('id', 'account_name', 'users', 'created')
  ```

  

- ```python
  class AccountSerializer(serializers.ModelSerializer):
      class Meta:
          model = Account
  ```

- 默认情况下，类上的所有模型字段都将映射到相应的序列化器字段。任何关系（例如模型上的外键）都将映射到`PrimaryKeyRelatedField`。其他模型字段将映射到相应的序列化器字段。

- 如果你希望在模型序列化器中使用默认字段的一部分，你可以使用`fields`或`exclude`选项来执行此操作，就像使用`ModelForm`一样。强烈建议你使用`fields`属性显式的设置要序列化的字段。这样就不太可能因为你修改了模型而无意中暴露了数据。

- 你还可以将`fields`属性设置成`'__all__'`来表明使用模型中的所有字段。

  ```python
  class AccountSerializer(serializers.ModelSerializer):
      class Meta:
          model = Account
          fields = '__all__'
  ```

  

- 你可以将`exclude`属性设置成一个从序列化器中排除的字段列表。

  ```python
  class AccountSerializer(serializers.ModelSerializer):
      class Meta:
          model = Account
          exclude = ('users',)
  ```

- 在上面的例子中，如果`Account`模型有三个字段`account_name`，`users`和`created`，那么只有 `account_name`和`created`会被序列化。

- 在`fields`和`exclude`属性中的名称，通常会映射到模型类中的模型字段。

- 或者`fields`选项中的名称可以映射到模型类中不存在任何参数的属性或方法。

## 指定嵌套序列化

- 默认`ModelSerializer`使用主键进行关联，但是你也可以使用`depth`选项轻松生成嵌套关联：

  ```python
  class AccountSerializer(serializers.ModelSerializer):
      class Meta:
          model = Account
          fields = ('id', 'account_name', 'users', 'created')
          depth = 1
  ```

- `depth`选项应该设置一个整数值，表明应该遍历的关联深度。

- 如果要自定义序列化的方式你需要自定义该子段。

## 指定字段的只读和只写

- 您可能希望将多个字段指定为只读。`read_only=True`您可以使用`read_only_fields`Meta选项，而不是使用属性显式添加每个字段，如下所示：

  ```python
  class AccountSerializer(serializers.ModelSerializer):
      class Meta:
          model = Account
          fields = ('id', 'account_name', 'users', 'created')
          read_only_fields = ('account_name',)
  ```

- 模型中已经设置`editable=False`的字段和默认就被设置为只读的`AutoField`字段都不需要添加到`read_only_fields`选项中。

- 您可能希望将多个字段指定为只写。`write_only=True`您可以使用`write_only_fields`Meta选项，而不是使用属性显式添加每个字段，如下所示：

  ```python
  class CreateUserSerializer(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = ('email', 'username', 'password')
          write_only_fields = ('password',)  # Note: Password field is write-only
  
      def restore_object(self, attrs, instance=None):
          """
          Instantiate a new User instance.
          """
          assert instance is None, 'Cannot update users with CreateUserSerializer'
          user = User(email=attrs['email'], username=attrs['username'])
          user.set_password(attrs['password'])
          return user
  ```

## 明确指定字段

- 您可以`ModelSerializer`通过在类上声明字段来添加或覆盖默认字段，就像对`Serializer`类一样。

  ```python
  class AccountSerializer(serializers.ModelSerializer):
      url = serializers.CharField(source='get_absolute_url', read_only=True)
      groups = serializers.PrimaryKeyRelatedField(many=True)
  
      class Meta:
          model = Account
  ```

- 额外字段可以对应于模型上的任何属性或可调用。

## `HyperlinkedModelSerializer`

- `HyperlinkedModelSerializer`类类似于`ModelSerializer`类，不同之处在于它使用超链接来表示关联关系而不是主键。

- 默认情况下序列化器将包含一个`url`字段而不是主键字段。

- url字段将使用`HyperlinkedIdentityField`字段来表示，模型的任何关联都将使用`HyperlinkedRelatedField`字段来表示。

- 你可以通过将主键添加到`fields`选项中来显式的包含，例如：

  ```python
  class AccountSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
          model = Account
          fields = ('url', 'id', 'account_name', 'users', 'created')
  ```

## 如何确定超链接视图

- 需要有一种方法来确定哪些视图应该用于超链接到模型实例。

- 默认情况下，预期超链接对应于与样式匹配的视图名称`'{model_name}-detail'`，并通过`pk`关键字参数查找实例。

- 您可以通过设置`lookup_field`选项来更改用于对象查找的字段。此选项的值应与URL conf中的kwarg以及模型上的字段对应。例如：

  ```python
  class AccountSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
          model = Account
          fields = ('url', 'account_name', 'users', 'created')
          lookup_field = 'slug'
  ```

- 请注意，`lookup_field`它将用作所有超链接字段的默认值，包括URL标识和任何超链接关系。

- 对于更具体的要求，例如为每个字段指定不同的查找，您需要明确设置序列化程序上的字段。例如：

  ```python
  class AccountSerializer(serializers.HyperlinkedModelSerializer):
      url = serializers.HyperlinkedIdentityField(
          view_name='account_detail',
          lookup_field='account_name'
      )
      users = serializers.HyperlinkedRelatedField(
          view_name='user-detail',
          lookup_field='username',
          many=True,
          read_only=True
      )
  
      class Meta:
          model = Account
          fields = ('url', 'account_name', 'users', 'created')
  ```



## 覆盖URL字段行为

- URL字段的名称默认为“url”。您可以使用该`URL_FIELD_NAME`设置全局覆盖此设置。

- 您还可以使用序列化程序上的`url_field_name`选项在每个序列化程序的基础上覆盖它，如下所示：

  ```python
  class AccountSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
          model = Account
          fields = ('account_url', 'account_name', 'users', 'created')
          url_field_name = 'account_url'
  ```

- **注意**：通用视图实现通常会生成一个`Location`标头以响应成功的`POST`请求。使用`url_field_name`选项的序列化程序不会自动包含此标头。如果您需要这样做，您将需要覆盖视图的`get_success_headers()`方法。

- 您还可以使用`view_name`和`lookup_field`选项覆盖URL字段的视图名称和查找字段，而无需显式覆盖该字段，如下所示：

  ```python
  class AccountSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
          model = Account
          fields = ('account_url', 'account_name', 'users', 'created')
          view_name = 'account_detail'
          lookup_field='account_name'
  ```

  