# ORM下的N+1问题

- ORM下数据库的N+1问题还是比较常见的，简单介绍一下。
- 这是下面讲解要使用到的模型类

```python

	# article/models.py
	class Article(models.Model):
    """博客文章模型类"""
    title = models.CharField(max_length=100, verbose_name="博客标题", unique=True)
    category = models.CharField(max_length=50, verbose_name="博客标签")
    pub_date = models.DateTimeField(auto_now_add=True, editable=True, verbose_name="发布时间")
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")
    content = models.TextField(blank=True, null=True, verbose_name="博客正文")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name


    # comment/models.py
    class Comment(models.Model):
    """文章评论模型类"""
    email = models.CharField(max_length=30, null=True, blank=True, verbose_name='邮箱')
    content = models.TextField(blank=True, null=True, verbose_name='评论内容')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True, verbose_name='评论时间')
    article = models.ForeignKey(Article, verbose_name='文章title', on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

```

- 上面两个模型类，文章模型类和评论模型类，在评论模型类中有一个ForeignKey模型字段将两个表进行关联。

## 如何产生N+1问题

- 当我们想获取"所有被评论过的文章信息（文章标题，文章分类）"时，需要
1. 查询所有评论；
2. 通过所有评论，获取被评论过的文章；
3. 获取这些文章的信息。

```python
	
	@api_view()
	def get_article_info_from_comment(request):
	    """通过评论，获取被评论过的文章信息"""
	    comments = models.Comment.objects.all()

	    article_list = []
	    for com in comments:
	        article_info = {}
	        article_info['title'] = com.article.title
	        article_info['category'] = com.article.category
	        article_list.append(article_info)

	    return Response(article_list)

```

- 结果

```json

	[
	    {
	        "title": "基于PyMySQL的数据库连接",
	        "category": "MySQL"
	    },
	    {
	        "title": "基于PyMySQL的数据库连接",
	        "category": "MySQL"
	    },
	    {
	        "title": "基于PyMySQL的数据库连接",
	        "category": "MySQL"
	    }
	]

```

- 数据库日志

```mysql
	
	(0.000) SELECT `comment_comment`.`id`, `comment_comment`.`email`, `comment_comment`.`content`, `comment_comment`.`pub_date`, `comment_comment`.`article_id` FROM `comment_comment`; args=()
	(0.002) SELECT `article_article`.`id`, `article_article`.`title`, `article_article`.`category`, `article_article`.`pub_date`, `article_article`.`update_time`, `article_article`.`content` FROM `article_article` WHERE `article_article`.`id` = 4; args=(4,)
	(0.001) SELECT `article_article`.`id`, `article_article`.`title`, `article_article`.`category`, `article_article`.`pub_date`, `article_article`.`update_time`, `article_article`.`content` FROM `article_article` WHERE `article_article`.`id` = 4; args=(4,)
	(0.001) SELECT `article_article`.`id`, `article_article`.`title`, `article_article`.`category`, `article_article`.`pub_date`, `article_article`.`update_time`, `article_article`.`content` FROM `article_article` WHERE `article_article`.`id` = 4; args=(4,)

```

- 可以看到，我们数据库只有3条数据，但是我们查询了数据4次(因为是先访问了一次评论表)
- 这就是N+1问题(我觉得更好的说法是1+N)
- 这样会导致的一个问题就是，当我们数据量过多时，回导致每次都访问一次数据库，这样对数据库造成不小的开销。
- 其实我们如果直接使用原生的mysql语句，一句就能解决，通过关联查询

```mysql

	select a.title, a.category
	from article_article a, comment_comment c
	where a.id = c.article_id;

```

- 虽然我们进行关联查询的时候会加大数据库的开销，但是当数据过多时，可以减少访问数据库的次数，这样也可以提升查询效率。

## 如何解决N+1问题

1. 数据库反范式设计,说直白点,就是把表合并,设计成冗余表,这可能会带来两个问题
	- 表中存在大量的重复数据项
	- 表中出现大量的空项,整个表格变成一个稀疏矩阵(sparse matrix)
	所以,这种方案显然存储效率不高,但是如果针对这两种情况进行优化,也算是是一种不错的解决办法,MongoDB就是这样干的

2. 加缓存 把整个列表页加上缓存. 这样 无论是继续执行1+N次查询,还是用inner join 1次查询搞定,都可以.
	这种方法的缺点是
	- 更新缓存 需要成本,增加了代码复杂度
	- 某些场景要求数据实时性,无法使用缓存

3. 把N+1次查询变成2次查询
	- 先查询出说有的评论ID
	- 然后通过这些评论ID查出所有的文章信息

## Django框架是如何解决N+1问题的

- select_related(), 通过关联查询，然后缓存
- prefetch_related(), 通过查询两次
- 有关这两个我在之前的文章中有介绍, [地址](https://blog.csdn.net/weixin_43182689/article/details/95320116)。

- 后记： 自己的一些粗略理解，如有不到之处或者错误欢迎指出，一起讨论。
- [参考文章](https://my.oschina.net/oncereply/blog/268922)

## 补充

- 稍微修改一下`get_article_info_from_comment`,通过`select_related()或prefetch_related()`进行优化。

```python
	
	@api_view()
	def get_article_info_from_comment(request):
	    """通过评论，获取被评论的文章信息, 修改版"""
	    # comments = models.Comment.objects.all().select_related('article')
	    comments = models.Comment.objects.all().prefetch_related('article')

	    article_list = []
	    for com in comments:
	        article_info = {}
	        article_info['title'] = com.article.title
	        article_info['category'] = com.article.category
	        article_list.append(article_info) 

	    return Response(article_list)      

```

- 使用了Django自带的，对N+1优化的两种方式，它们访问数据库的情况分别为。

```mysql

	(0.001) SELECT `comment_comment`.`id`, `comment_comment`.`email`, `comment_comment`.`content`, `comment_comment`.`pub_date`, `comment_comment`.`article_id`, `article_article`.`id`, `article_article`.`title`, `article_article`.`category`, `article_article`.`pub_date`, `article_article`.`update_time`, `article_article`.`content` FROM `comment_comment` INNER JOIN `article_article` ON (`comment_comment`.`article_id` = `article_article`.`id`); args=()

```

```mysql
	
	(0.001) SELECT `comment_comment`.`id`, `comment_comment`.`email`, `comment_comment`.`content`, `comment_comment`.`pub_date`, `comment_comment`.`article_id` FROM `comment_comment`; args=()
	(0.000) SELECT `article_article`.`id`, `article_article`.`title`, `article_article`.`category`, `article_article`.`pub_date`, `article_article`.`update_time`, `article_article`.`content` FROM `article_article` WHERE `article_article`.`id` IN (4); args=(4,)

```