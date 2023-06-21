# 字段查询

- 字段查询是指如何指定`SQL WHERE` 子句的内容。它们通过查询集方法filter()、exclude() 和 get() 的关键字参数指定。

- 查询的关键字参数的基本形式是`field__lookuptype=value`。（中间是两个下划线）。例如：

  ```python
  Entry.objects.filter(pub_date__lte='2006-01-01')
  ```

- 翻译成SQL（大体）是：

  ```mysql
  SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';
  ```

- 这是如何实现的，Python 定义的函数可以接收任意的键/值对参数，这些名称和参数可以在运行时求值。更多信息，参见Python 官方文档中的关键字参数。

- 查询条件中指定的字段必须是模型字段的名称。但有一个例外，对于ForeignKey你可以使用字段名加上_id 后缀。在这种情况下，该参数的值应该是外键的原始值。

## 跨关联关系的查询

- Django 提供一种强大而又直观的方式来“处理”查询中的关联关系，它在后台自动帮你处理`JOIN`。 若要跨越关联关系，只需使用关联的模型字段的名称，**并使用双下划线分隔**，直至你想要的字段：

  ```python
  from django.db import models
  
  # Create your models here.
  
  
  class Question(models.Model):
      question_text = models.CharField(max_length=200)
      pub_date = models.DateTimeField('data published', default="")
  
      def __str__(self):
          return self.question_text
  
  
  class Chioce(models.Model):
      question = models.ForeignKey(Question)
      choice_text = models.CharField(max_length=200)
      votes = models.IntegerField(default=0)
  
      def __str__(self):
          return self.choice_text
  
  ```

- 获取所有Question的question_text为"q2"的Chioce对象

  ```python
  Chioce.objects.filter(question__question_text="q2")
  [<Chioce: c2>, <Chioce: c6>, <Chioce: c7>]
  ```

- 这种跨越可以是任意的深度。

- 它还可以反向工作。若要引用一个“反向”的关系，**只需要使用该模型的小写的名称**，`modelclassname__fieldname`。

## 如何获取choices属性的值

- 由二项元组构成的一个可迭代对象（例如，列表或元组），用来给字段提供选择项。 如果设置了choices ，默认的表单将是一个选择框而不是标准的文本框，而且这个选择框的选项就是choices 中的选项。

  ```python
  from django.db import models
  
  class Person(models.Model):
      SHIRT_SIZES = (
          ('S', 'Small'),
          ('M', 'Medium'),
          ('L', 'Large'),
      )
      name = models.CharField(max_length=60)
      shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
  ```

- 每个元组中的第一个元素，是存储在数据库中的值；第二个元素是在管理界面或 ModelChoiceField 中用作显示的内容。 在一个给定的 model 类的实例中，想得到某个 choices 字段的显示值，就调用 `get_FOO_display` 方法(这里的 FOO 就是 choices 字段的名称 )

  ```python
  >>> p = Person(name="Fred Flintstone", shirt_size="L")
  >>> p.save()
  >>> p.shirt_size
  'L'
  >>> p.get_shirt_size_display()
  'Large'
  ```

  