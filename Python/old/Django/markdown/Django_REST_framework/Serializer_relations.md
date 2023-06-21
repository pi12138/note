# `Serializer relations`

- 关系字段用于表示模型关系。它们可以应用到`ForeignKey`，`ManyToManyField`和`OneToOneField`关系，以及扭转的关系，以及自定义关系等`GenericForeignKey`。

  ------

- **注意：**关系字段是声明的`relations.py`，但按照惯例，您应该从`serializers`模块中导入它们，使用`from rest_framework import serializers`并将字段引用为`serializers.<FieldName>`。

## `RelationField`

- `RelatedField`可以用来表示使用其`__unicode__`方法的关系的目标。

- 该字段是只读的。

- **参数**：

  - `many`- 如果应用于多对多关系，则应将此参数设置为`True`。

  ```python
  # models.py
  
  from django.db import models
  
  # Create your models here.
  
  
  class Album(models.Model):
      album_name = models.CharField(max_length=100)
      artist = models.CharField(max_length=100)
  
  
  class Track(models.Model):
      album = models.ForeignKey(Album, related_name="tracks")
      order = models.IntegerField()
      title = models.CharField(max_length=100)
      duration = models.IntegerField()
  
      class Meta:
          unique_together = ('album', 'order')
          # order_by = 'order'
  
      def __unicode__(self):
          return "{}: {}".format(self.order, self.title)
  
  ```

  

  ```python
  # serializers.py
  
  from rest_framework import serializers
  from .models import Album, Track
  
  
  class AlbumSerializer(serializers.ModelSerializer):
      tracks = serializers.RelatedField(many=True)
  
      class Meta:
          model = Album
          fields = ('album_name', 'artist', 'tracks')
  
  
  class TrackSerializer(serializers.ModelSerializer):
      class Meta:
          model = Track
          fields = ('album', 'order', 'title', 'duration')
  
  ```

  

- 序列化输出如下

  ```json
  {
      "album_name": "1", 
      "artist": "1", 
      "tracks": [
          "0: a"
      ]
  }
  ```

## `PrimaryKeyRelatedField`

- `PrimaryKeyRelatedField` 可以用于使用其主键表示关系的目标。

- 默认情况下，此字段是读写的，但您可以使用该`read_only`标志更改此行为。

  **参数**：

  - `many`- 如果应用于多对多关系，则应将此参数设置为`True`。
  - `required`- 如果设置为`False`，则该字段将接受`None`可为空的关系的值或空字符串。
  - `queryset`- 默认情况下，`ModelSerializer`类将使用关系的默认查询集。 `Serializer`类必须显式设置查询集，或者设置`read_only=True`。

  ```python
  from rest_framework import serializers
  from .models import Album, Track
  
  
  class AlbumSerializer(serializers.ModelSerializer):
      tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  
      class Meta:
          model = Album
          fields = ('album_name', 'artist', 'tracks')
  
  
  class TrackSerializer(serializers.ModelSerializer):
      class Meta:
          model = Track
          fields = ('album', 'order', 'title', 'duration')
  
  ```

- 序列化输入如下

  ```json
  {
      "album_name": "1", 
      "artist": "1", 
      "tracks": [
          1
      ]
  }
  ```

## `HyperlinkedRelatedFiedl`

- `HyperlinkedRelatedField` 可以用于使用超链接表示关系的目标。

- 默认情况下，此字段是读写的，但您可以使用该`read_only`标志更改此行为。

  **参数**：

  - `view_name` - 应该用作关系目标的视图名称。如果您使用的[是标准路由器类](http://tomchristie.github.io/rest-framework-2-docs/api-guide/routers#defaultrouter)，则该格式为字符串`<modelname>-detail`。**要求**。
  - `many`- 如果应用于多对多关系，则应将此参数设置为`True`。
  - `required`- 如果设置为`False`，则该字段将接受`None`可为空的关系的值或空字符串。
  - `queryset`- 默认情况下，`ModelSerializer`类将使用关系的默认查询集。 `Serializer`类必须显式设置查询集，或者设置`read_only=True`。
  - `lookup_field` - 目标上应该用于查找的字段。应该对应于引用视图上的URL关键字参数。默认是`'pk'`。
  - `format`- 如果使用格式后缀，超链接字段将为目标使用相同的格式后缀，除非使用`format`参数覆盖。

  ```python
  class AlbumSerializer(serializers.ModelSerializer):
      tracks = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="track-detail")
  
      class Meta:
          model = Album
          fields = ('album_name', 'artist', 'tracks')
  
  ```

- 序列化输出结果

  ```json
  {
      "album_name": "1", 
      "artist": "1", 
      "tracks": [
          "http://127.0.0.1:8000/test1/tracks/1/"
      ]
  }
  ```

## `SlugRelatedField`

- `SlugRelatedField` 可以用于使用目标上的字段来表示关系的目标。

- 默认情况下，此字段是读写的，但您可以使用该`read_only`标志更改此行为。

  当`SlugRelatedField`用作读写字段时，通常需要确保slug字段对应于带有的模型字段`unique=True`。

  **参数**：

  - `slug_field` - 目标上应该用于表示它的字段。这应该是唯一标识任何给定实例的字段。例如，`username`。 **需要**
  - `many`- 如果应用于多对多关系，则应将此参数设置为`True`。
  - `required`- 如果设置为`False`，则该字段将接受`None`可为空的关系的值或空字符串。
  - `queryset`- 默认情况下，`ModelSerializer`类将使用关系的默认查询集。 `Serializer`类必须显式设置查询集，或者设置`read_only=True`。

  ```python
  class AlbumSerializer(serializers.ModelSerializer):
      tracks = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
  
      class Meta:
          model = Album
          fields = ('album_name', 'artist', 'tracks')
  ```

- 序列化输出数据

  ```json
  {
      "count": 2, 
      "next": null, 
      "previous": null, 
      "results": [
          {
              "album_name": "1", 
              "artist": "1", 
              "tracks": [
                  "a", 
                  "This is a title"
              ]
          }, 
          {
              "album_name": "2", 
              "artist": "2", 
              "tracks": []
          }
      ]
  }
  ```

## `HyperlinkedIdentityField`

- 此字段可以作为标识关系应用，例如`'url'`HyperlinkedModelSerializer上的字段。它也可以用于对象的属性。

- 该字段始终为只读。

  **参数**：

  - `view_name` - 应该用作关系目标的视图名称。如果您使用的[是标准路由器类](http://tomchristie.github.io/rest-framework-2-docs/api-guide/routers#defaultrouter)，则该格式为字符串`<model_name>-detail`。 **要求**。
  - `lookup_field` - 目标上应该用于查找的字段。应该对应于引用视图上的URL关键字参数。默认是`'pk'`。
  - `format`- 如果使用格式后缀，超链接字段将为目标使用相同的格式后缀，除非使用`format`参数覆盖。

  ```python
  class AlbumSerializer(serializers.ModelSerializer):
      tracks = serializers.HyperlinkedIdentityField(view_name='track-detail')
  
      class Meta:
          model = Album
          fields = ('album_name', 'artist', 'tracks')
  
  ```

- 序列化输出结果

  ```json
  {
      "album_name": "1", 
      "artist": "1", 
      "tracks": "http://127.0.0.1:8000/test1/tracks/1/"
  }
  ```

  