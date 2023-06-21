# 模型类关系

- Django中模型类关系字段主要有三种
  - ForeighKey
  - ManyToManyField
  - OneToOneField

## ForeignKey

### 前向查询

- 如果模型具有一个 ForeignKey ，那么该模型的实例将可以通过属性访问关联的（外部）对象。
- 前向查询一对多关联关系时在第一次访问关联对象就被缓存。以后对同一个对象的外键的访问都使用缓存。
- QuerySet 的 select_related() 方法预先递归填充所有的一对多关系到缓存中。

### 反向查询

- 如果模型具有外键 ForeignKey ，那么该外键所指向的模型实例可以通过 Manager 返回包含某个特定外键的源模型的所有实例。 

- 模型情况下，这个 Manager 叫做 foo_set, foo 是源模型的小写名称。 该 Manager 返回的 QuerySets 同样可以使用过滤等操作（get(), all(), filter()....）。

  ```python
  >>> from apps.books.models import Publisher
  >>> pub = Publisher.objects.get(id=3)
  >>> pub
  <Publisher: p1>
  >>> pub.book_set.all()
  [<Book: b1>, <Book: b2>]
  >>> pub.book_set.all()
  ```

- 你可以在定义 ForeignKey 时 设置 related_name 参数来重写 foo_set 名字。

## ManyToManyField

- ``ManyToManyField(to, **options)`，多对多的关系，需要一个位置参数，相关的模型类

### 多对多关系模型类查询

- 多对多关系的两端都带有访问另一端的API， 唯一的区别在于属性的名称，`ManyToManyField`的模型使用本字段的属性名称，而"反向"模型使用源模型的小写名称加上 `'_set'`

  - 正向查询，直接通过模型类中的字段进行查询，使用（.）点号进行访问
  - 注意：多对多关系虽然和外键关系还有一对一关系都是通过点（.）可以访问，但是他们的返回内容是不一样的，外键关系和一对一关系返回的是一个模型类对象，而多对多关系返回的是一个QuerySet，我们可以对它进行QuerySet的一些操作（.all()，.filter()）。

  ```python
  # 通过 Book模型类的 ManyToManyField 字段authors 查询 Author 模型类内容
  >>> from apps.books.models import Book
  >>> book = Book.objects.get(id=3)
  >>> book.authors.all()
  [<Auther: a1>]
  >>> book.author.count()
  ```

  - 反向查询，通过关联模型类名（小写），`ModelClassName_set`，进行查询

  ```python
  >>> author = Auther.objects.get(id=2)
  >>> author.book_set.all()
  [<Book: b1>, <Book: b2>, <Book: b3>]
  ```

- 类似 ForeignKey, ManyToManyField 可以指定 related_name 。在上面的例子中， 如果 Book 中的 ManyToManyField 指定 related_name='books', 那么 Author 实例将使用 books 属性而不是 book_set 。

  - 对ManyToManyField字段添加 related_name='books' 参数后进行反向查询

    ```python
    >>> from apps.books.models import Auther
    >>> author = Auther.objects.get(id=2)
    >>> author.books.all()
    [<Book: b1>, <Book: b2>, <Book: b3>]
    ```


## OneToOneField

### 反向查询

- 一对一的反向查询和多对多，多对一稍微有些不同，

- 通过关联对象模型类名（小写）`.modelclassname`，如：下面co是Code模型类的对象，Nation和Code是OneToOneField.

  ```python
  >>> co.nation
  <nation: n2>
  >>> co.nation.id
  2
  ```

  