# 数据库查询优化（二）

- [接上回写过的文章](https://blog.csdn.net/weixin_43182689/article/details/95320116)

- 下面将会使用到的模型类

    ```python
    class Article(models.Model):
        """博客文章模型类"""
        title = models.CharField(max_length=100, verbose_name="博客标题", unique=True)
        category = models.CharField(max_length=50, verbose_name="博客标签")
        pub_date = models.DateTimeField(auto_now_add=True, editable=True, verbose_name="发布时间")
        update_time = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")
        content = models.TextField(blank=True, null=True, verbose_name="博客正文")
    
        def __str__(self):
            return self.title
    ```

    

## 使用QuerySet.exists()判断查询集是否为空

- 通常情况下，我们习惯使用 `if queryset`来判断查询集是否为空，这样会从数据库取出查询集中的所有数据

- 使用`if queryset.exists()`，只会从数据库中取一条数据。

    ```python
    >>> from apps.article.models import Article
    >>> arts = Article.objects.all()
    >>> arts.exists()
    True
    >>> arts
    ```

    - `arts.exists()`执行的查询

    ```mysql
    (0.000) SELECT (1) AS `a` FROM `article_article`  LIMIT 1; args=()
    ```

    - `arts`执行的查询

    ```mysql
    (0.001) SELECT `article_article`.`id`, `article_article`.`title`, `article_article`.`category`, `article_article`.`pub_date`, `article_article`.`update_time`, `article_article`.`content` FROM `article_article`  LIMIT 21; args=()
    ```

## 使用QuerySet.count()获取查询集数据个数

- 通常情况下，我们习惯于使用`len()`获取一个对象中的数据个数，但是`len(queryset)`这样会从数据库取出查询集中的所有数据。

- 使用`queryset.count()`,会直接使用数据库计数函数`count()`来计算数据个数，当数据量较大时会节省查询时间。

    ```python
    >>> from apps.article.models import Article
    >>> arts = Article.objects.all()
    >>> arts.count()
    24
    >>> len(arts)
    24
    ```

    - `arts.count()`执行的查询

    ```mysql
    (0.001) SELECT COUNT(*) AS `__count` FROM `article_article`; args=()
    ```

    - `len(arts)`执行的查询

    ```mysql
    (0.002) SELECT `article_article`.`id`, `article_article`.`title`, `article_article`.`category`, `article_article`.`pub_date`, `article_article`.`update_time`, `article_article`.`content` FROM `article_article`; args=()
    ```

## 使用values()或者values_list()取需要的数据列

- 大多数，一个数据表中的数据列，我们只会用到其中的一列或者两列，这时就没有必要从数据库中查询其他列的数据，使用 `quertset.values(*field)`可以取指定的数据列。

    ```python
    >>> from apps.article.models import Article
    >>> arts = Article.objects.all()
    >>> for art in arts.values('title'):
    ...     print(art['title'])
    ...
    基于PyMySQL的数据库连接
    Django中如何使用markdown
    Django全文检索
    ...
    >>> for art in arts:
    ...     print(art.title)
    ...
    基于PyMySQL的数据库连接
    Django中如何使用markdown
    Django全文检索
    ....
    ```

    - 执行的sql语句

    ```mysql
    (0.001) SELECT `article_article`.`title` FROM `article_article`; args=()
    (0.002) SELECT `article_article`.`id`, `article_article`.`title`, `article_article`.`category`, `article_article`.`pub_date`, `article_article`.`update_time`, `article_article`.`content` FROM `article_article`; args=()
    ```

## 小结

- 这几种方法都没有改变查询数据库的次数，主要优化在减少从数据库中取出的数据量，以此来加快查询速度。