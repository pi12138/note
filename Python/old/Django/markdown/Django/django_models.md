# 1.定义模型
- 步骤
  - step1： 在models.py 中定义模型类
  - step2： 在settings.py --> INSTALLED_APPS 注册应用
  - step3： 根据模型类生成迁移文件
       python manage.py makemigrations
       	  ### 如果 app 较多，想指定app迁移，
       	  使用 python manage.py makemigrations app_name
  - step4： 根据迁移文件在数据库中生成表
       python manage.py migrate
### 1.备注：python manage.py dbshell 可以直接进入项目已经连接的数据库
	    python manage.py shell 可以进入python shell 进行简单模型api练习两种有所不同

### 2.备注： django-关于manage.py migrate无效的问题 
- [参考博客](https://blog.csdn.net/qq_25730711/article/details/60327344)

### 3.备注： 数据迁移到数据库表后，表 django_migrations 中保存有迁移的app信息，如果修改模型后重新迁移，需要先删除该表中的一部分内容

- 元选项
  - 在模型类中定义类 "Meta", 用于设置元信息
  - db_table：自定义数据表名称，推荐使用小写字母
    - 默认情况下数据表名称为 <app_name>_<model_name>
  - verbose_name： 自定义后台数据表名，可以改成中文
  - verbose_name_plural: 后台数据表名的复数，通常可以写成`verbose_name_plural = verbose_name`
  - ordering:对象默认排序字段，获取对象的列表时使用，接收属性构成的列表
    - ordering = ['id'..]
    - 字符串前加 "-"(减号) 表示倒序不加表示正常
      - ordering = ['-id']
    - 排序会增加数据库开销

## 字段类型

- AutoField：一个根据实际ID自动增长的IntegerField，通常不指定
  - 如果不指定，一个主键字段将自动添加到模型中
- BooleanField：true/false 字段，此字段的默认表单控制是CheckboxInput
- NullBooleanField：支持null、true、false三种值
- CharField(max_length=字符长度)：字符串，默认的表单样式是 TextInput
- TextField：大文本字段，一般超过4000使用，默认的表单控件是Textarea
- IntegerField：整数
- DecimalField(max_digits=None, decimal_places=None)：使用python的Decimal实例表示的十进制浮点数
  - DecimalField.max_digits：位数总数
  - DecimalField.decimal_places：小数点后的数字位数
- FloatField：用Python的float实例来表示的浮点数
- DateField[auto_now=False, auto_now_add=False])：使用Python的datetime.date实例表示的日期
  - 参数DateField.auto_now：每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false
  - 参数DateField.auto_now_add：当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false
  - 该字段默认对应的表单控件是一个TextInput. 在管理员站点添加了一个JavaScript写的日历控件，和一个“Today"的快捷按钮，包含了一个额外的invalid_date错误消息键
  - auto_now_add, auto_now, and default 这些设置是相互排斥的，他们之间的任何组合将会发生错误的结果
- TimeField：使用Python的datetime.time实例表示的时间，参数同DateField
- DateTimeField：使用Python的datetime.datetime实例表示的日期和时间，参数同DateField
- FileField：一个上传文件的字段
- ImageField：继承了FileField的所有属性和方法，但对上传的对象进行校验，确保它是个有效的image

#### 字段选项

- 通过字段选项，可以实现对字段的约束
- 在字段对象时通过关键字参数指定
- null：如果为True，Django 将空值以NULL 存储到数据库中，默认值是 False
- blank：如果为True，则该字段允许为空白，默认值是 False
- **对比：null是数据库范畴的概念，blank是表单验证证范畴的**
- db_column：字段的名称，如果未指定，则使用属性的名称
- db_index：若值为 True, 则在表中会为此字段创建索引
- default：默认值
- primary_key：若为 True, 则该字段会成为模型的主键字段
- unique：如果为 True, 这个字段在表中必须有唯一值
- verbose_name：后台数据字段的名称，如果未指定，则使用属性的名称。可以修改后台的数据字段名称。
- choices:限定取值范围。 

# 2.自连接

- 自连接在构建模型类的"外键"时和一般连接方式有所不同
	- 自连接：
		```python
		parents = models.ForeignKey('self', null=True, blank=True)
		```
	- 一般连接：
		```python
		book = models.ForeignKey('BookInfo')
		# BookInfo 为另一个类
		```



# 管理器Manager

- 管理器是模型类的一个属性，用于将对象和数据表映射
- 每个模型类当作至少有一个管理器属性，如果不创建默认为 objects
- 管理器是用来和数据库进行交互的，没有管理器就无法和数据库进行交互
- objects：是Manager类型的对象，用于与数据库进行交互

### 自定义Manager

- 自定义Manager的目的

  - 增加默认的manager方法
  - 或修改manager返回的初始QuerySet

- 如何自定义Manager

  - 自定义一个manager类，继承`django.db.models.Manager`

    ```python
    # managers.py
    from django.db import models
    class BookManager(models.Manager):
        """自定义Book管理器类"""
    
        def book_count(self):
            """统计模型类对象总数"""
            return self.all().count()
    
    # models.py Book
    class Book(models.Model):
        # 实例化管理器，不一定要命名为objects
        objects = BookManager()
    
    ```

  - 测试自定义的管理器新添加的方法title_count()

    ```python
    >>> book = Book.objects.all()
    >>> book
    [<Book: b1>, <Book: b2>, <Book: b3>, <Book: b4>, <Book: b5>]
    >>> book_num = Book.objects.book_count()
    >>> book_num
    5
    ```

### 修改初始的Manager QuerySet

- .objects.all()通常情况下会返回模型类的所有对象，我们可以通过重写Manager.get_queryset()方法来修改其功能

  ```python
  # managers.py
  class MaleManager(models.Manager):
      def get_queryset(self):
          """返回所有男性对象"""
          return super(MaleManager, self).get_queryset().filter(gender='M')
  class FemaleManager(models.Manager):
      def get_queryset(self):
          """返回所有女性对象"""
          return super(FemaleManager, self).get_queryset().filter(gender="F")
      
  # models.py
  class People(models.Model):
      gender_limit = (
          ('M', 'Male'),
          ('F', 'Female'),
      )
  
      name = models.CharField(max_length=30)
      gender = models.CharField(max_length=1, choices=gender_limit)
  
      # 定义多个管理器
      people = models.Manager()
      male = MaleManager()
      female = FemaleManager()
  
      def __str__(self):
          return self.name
  ```

  - 此处定义了多个管理器

  ```python
  >>> from apps.books.models import People
  >>> People.people.all()
  [<People: aaa>, <People: bbb>, <People: ccc>, <People: ddd>, <People: eee>, <People: fff>]
  >>> People.male.all()
  [<People: aaa>, <People: bbb>, <People: ccc>]
  >>> People.female.all()
  [<People: ddd>, <People: eee>, <People: fff>]
  ```

- 如果你使用自定义的`Manager`对象，请注意，Django遇到的第一个Manager(以它在模型中被定义的位置为准)会有一个特殊状态。 Django将会把第一个`Manager` 定义为默认`Manager` ，Django的许多部分(但是不包括admin应用)将会明确地为模型使用这个`manager`。 你应该小心地选择你的默认manager。因为覆盖`get_queryset()` 了，你可能接受到一个无用的返回对像，你必须避免这种情况。



## 模型类操作

### 新建保存数据

- 通常情况下，需要使用.save()来在最后保存数据
- 也可以使用 ModelClass.objects.create() **来同时创建并且保存新数据**

### 更新数据

- 通常情况下，对数据的更新，要先获取数据，然后修改数据，然后执行.save()方法，
- 但是，执行save()方法，会这个方法会更新一行里的所有列。 而通常情况下，我们只需要更新行里的某几列。
- 为了更改指定的某一列，可以使用结果集（QuerySet）对象的update()方法。
- update()方法对于结果集（QuerySet）中全部内容均有效，这意味着你可以同时更新多条记录。
- update()方法返回被修改数据的条数，**注意：update()是对查询集进行操作，而不是单个对象**

### 删除数据

- 删除数据使用.delete()方法
- 该方法既可以删除单条数据，也可以通过查询集删除多条数据



## 模型类查询

- 通常情况下，查询模型类返回的模型对象格式是这样的

  ```python
  [<Publisher: Publisher object>, <Publisher: Publisher object>]
  ```

- 这样只能看出有几条数据，去不能确定每个对象的独特信息

- 如果想要让对象返回信息，需要在模型类中定义`__str__()`方法，并返回该对象的信息（python2是`__unicode__`

  ```python
      def __str__(self):
          return self.name
  ```

- 重写`__str__`方法后，查询模型类返回内容格式是这样的

  ```python
  [<Publisher: Apress>, <Publisher: O'Reilly>]
  ```

  