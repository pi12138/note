# 数据库查询优化（一）

- 主要优化方式还是通过尽可能的减少访问数据库的次数。

## 1. QuerySet如何工作

- Django QuerySet是懒执行的，**只有访问到对应数据的时候**，**才会去访问数据库**。
- 另外如果你再次读取查询到的数据，将不会触发数据库的访问。

- 例如：请求下面视图，不会进行数据库查询操作，尽管进行了模型类查询

  ```python
  class BookView(View):
      """
      book class
      """
      def get(self, request, *args, **kwargs):
          
          books = models.Book.objects.all()
          
          return HttpResponse("....")
  ```

- 下面对数据进行读取，日志文件中会显示，进行了一次数据库查询。

  ```python
      def get(self, request, *args, **kwargs):
          books = models.Book.objects.all()
  		
          # 此处会读取数据库
          if books:
              print(books)
  
          book_list = []
          # 再次读取数据，但是不会再访问数据库
          for book in books:
              book_info = {}
              book_info['title'] = book.title
              # book_info['authors'] = book.authors
              book_list.append(book_info)
  
          return JsonResponse(book_list, safe=False)
  ```

  ```sqlite
  (0.001) QUERY = 'SELECT "books_book"."id", "books_book"."title", "books_book"."publisher_id", "books_book"."publication_date" FROM "books_book"' - PARAMS = (); args=()
  ```

## 2. 使用select_related 和 prefetch_related

- 这两个函数主要是用来优化关联查询的情况，当需要进行关联查询时，如果编写不正确的话，Django 将会多次访问库进行查询，我们应该避免这种情况。尤其是当查询语句位于某个循环中的时候，会导致只需要执行一次的查询重复执行多次。

### select_related()

-  select_related() 通过多表join关联查询，一次性获得所有数据，通过降低数据库查询次数来提升性能，但关联表不能太多，因为join操作本来就比较消耗性能。

- publisher是Book模型类的外键，通过外键访问表Publisher获取name，下面有5个Book对象，访问了数据库6次。

  ```python
  def get_book_publisher(request):
      """获取每本书的出版社"""
      books = models.Book.objects.all()
  
      book_list = []
      for book in books:
          book_info = {}
          book_info[book.title] = book.publisher.name
          book_list.append(book_info)
  
      return JsonResponse(book_list, safe=False)
  ```

  ```sqlite
  (0.001) QUERY = 'SELECT "books_book"."id", "books_book"."title", "books_book"."publisher_id", "books_book"."publication_date" FROM "books_book"' - PARAMS = (); args=()
  (0.001) QUERY = 'SELECT "books_publisher"."id", "books_publisher"."name", "books_publisher"."address", "books_publisher"."city", "books_publisher"."state_province", "books_publisher"."country", "books_publisher"."website" FROM "books_publisher" WHERE "books_publisher"."id" = %s' - PARAMS = (3,); args=(3,)
  (0.000) QUERY = 'SELECT "books_publisher"."id", "books_publisher"."name", "books_publisher"."address", "books_publisher"."city", "books_publisher"."state_province", "books_publisher"."country", "books_publisher"."website" FROM "books_publisher" WHERE "books_publisher"."id" = %s' - PARAMS = (3,); args=(3,)
  (0.000) QUERY = 'SELECT "books_publisher"."id", "books_publisher"."name", "books_publisher"."address", "books_publisher"."city", "books_publisher"."state_province", "books_publisher"."country", "books_publisher"."website" FROM "books_publisher" WHERE "books_publisher"."id" = %s' - PARAMS = (4,); args=(4,)
  (0.000) QUERY = 'SELECT "books_publisher"."id", "books_publisher"."name", "books_publisher"."address", "books_publisher"."city", "books_publisher"."state_province", "books_publisher"."country", "books_publisher"."website" FROM "books_publisher" WHERE "books_publisher"."id" = %s' - PARAMS = (4,); args=(4,)
  (0.000) QUERY = 'SELECT "books_publisher"."id", "books_publisher"."name", "books_publisher"."address", "books_publisher"."city", "books_publisher"."state_province", "books_publisher"."country", "books_publisher"."website" FROM "books_publisher" WHERE "books_publisher"."id" = %s' - PARAMS = (7,); args=(7,)
  
  ```

- 使用 select_related 进行优化，对数据库进行了JOIN查询，但是只访问了数据库一次

  ```python
  def get_book_publisher(request):
      """获取每本书的出版社, 优化版"""
      books = models.Book.objects.all().select_related('publisher')
  
      book_list = []
      for book in books:
          book_info = {}
          book_info[book.title] = book.publisher.name
          book_list.append(book_info)
  
      return JsonResponse(book_list, safe=False)
  ```

  ```sqlite
  (0.001) QUERY = 'SELECT "books_book"."id", "books_book"."title", "books_book"."publisher_id", "books_book"."publication_date", "books_publisher"."id", "books_publisher"."name", "books_publisher"."address", "books_publisher"."city", "books_publisher"."state_province", "books_publisher"."country", "books_publisher"."website" FROM "books_book" INNER JOIN "books_publisher" ON ( "books_book"."publisher_id" = "books_publisher"."id" )' - PARAMS = (); args=()
  ```

- 上面的例子是Book表和Publisher两个表的外键关联，如果此时有第三个表的加入呢，例如新加入一个表Country用来保存出版社的地址，现在我们要查询每本书的出版社地址

  ```python
  def get_book_publisher_country(request):
      """获取每本书的出版社的地址"""
      books = models.Book.objects.all().select_related("publisher")
  
      book_list = []
      for book in books:
          book_info = (book.title, book.publisher.name, book.publisher.country.country)
          book_list.append(book_info)
  
      return JsonResponse(book_list, safe=False)
  ```

  ```sqlite
  (0.000) QUERY = 'SELECT "books_book"."id", "books_book"."title", "books_book"."publisher_id", "books_book"."publication_date", "books_publisher"."id", "books_publisher"."name", "books_publisher"."address", "books_publisher"."city", "books_publisher"."state_province", "books_publisher"."country_id", "books_publisher"."website" FROM "books_book" INNER JOIN "books_publisher" ON ( "books_book"."publisher_id" = "books_publisher"."id" )' - PARAMS = (); args=()
  (0.001) QUERY = 'SELECT "books_country"."id", "books_country"."country" FROM "books_country" WHERE "books_country"."id" = %s' - PARAMS = (3,); args=(3,)
  (0.001) QUERY = 'SELECT "books_country"."id", "books_country"."country" FROM "books_country" WHERE "books_country"."id" = %s' - PARAMS = (3,); args=(3,)
  (0.000) QUERY = 'SELECT "books_country"."id", "books_country"."country" FROM "books_country" WHERE "books_country"."id" = %s' - PARAMS = (1,); args=(1,)
  (0.001) QUERY = 'SELECT "books_country"."id", "books_country"."country" FROM "books_country" WHERE "books_country"."id" = %s' - PARAMS = (1,); args=(1,)
  (0.000) QUERY = 'SELECT "books_country"."id", "books_country"."country" FROM "books_country" WHERE "books_country"."id" = %s' - PARAMS = (2,); args=(2,)
  ```

- 因为有了第三个表的加入，获取第三个表的数据时，又访问了5次数据库

- 继续借助 select_related 进行优化，只不过这次稍微有些不同，涉及到深层查询，需要通过'__'(双下划线)来连接字段，实现递归查询。

- 下面对原来的内容进行简单修改后，获取数据时，只访问了1次数据库。

  ```python
  def get_book_publisher_country(request):
      """获取每本书的出版社的地址, 优化版"""
      books = models.Book.objects.all().select_related("publisher__country")
  
      book_list = []
      for book in books:
          book_info = (book.title, book.publisher.name, book.publisher.country.country)
          book_list.append(book_info)
  
      return JsonResponse(book_list, safe=False)
  ```

  ```sqlite
  (0.002) QUERY = 'SELECT "books_book"."id", "books_book"."title", "books_book"."publisher_id", "books_book"."publication_date", "books_publisher"."id", "books_publisher"."name", "books_publisher"."address", "books_publisher"."city", "books_publisher"."state_province", "books_publisher"."country_id", "books_publisher"."website", "books_country"."id", "books_country"."country" FROM "books_book" INNER JOIN "books_publisher" ON ( "books_book"."publisher_id" = "books_publisher"."id" ) INNER JOIN "books_country" ON ( "books_publisher"."country_id" = "books_country"."id" )' - PARAMS = (); args=()
  ```

### select_related总结

1. select_related主要针对 ForeignKey 或 OneToOneField 的关系进行优化。

2. select_related使用SQL的JOIN语句进行优化，通过减少SQL查询的次数来进行优化、提高性能。

3. 当需要深层查询（递归查询）时，可以通过使用双下划线“__”连接字段名来实现指定的递归查询（也就是外键的外键，多层连表查询）。

### prefetch_related()

- Auther模型类和Book模型类是多对多的关系，通过Book查找每本书的作者，访问了数据库6次

  ```python
  def get_book_authors(request):
      """
      获取每本书的作者
      """
      books = models.Book.objects.all()
  
      book_list = []
      for book in books:
          book_info = {}
          book_info['book'] = book.title
          book_info['authors'] = [author.first_name for author in book.authors.all()]
          book_list.append(book_info)
  
      return JsonResponse(book_list, safe=False)
  ```

  ```sqlite
  (0.001) QUERY = 'SELECT "books_book"."id", "books_book"."title", "books_book"."publisher_id", "books_book"."publication_date" FROM "books_book"' - PARAMS = (); args=()
  (0.000) QUERY = 'SELECT "books_auther"."id", "books_auther"."first_name", "books_auther"."last_name", "books_auther"."email" FROM "books_auther" INNER JOIN "books_book_authors" ON ( "books_auther"."id" = "books_book_authors"."auther_id" ) WHERE "books_book_authors"."book_id" = %s' - PARAMS = (3,); args=(3,)
  (0.000) QUERY = 'SELECT "books_auther"."id", "books_auther"."first_name", "books_auther"."last_name", "books_auther"."email" FROM "books_auther" INNER JOIN "books_book_authors" ON ( "books_auther"."id" = "books_book_authors"."auther_id" ) WHERE "books_book_authors"."book_id" = %s' - PARAMS = (4,); args=(4,)
  (0.000) QUERY = 'SELECT "books_auther"."id", "books_auther"."first_name", "books_auther"."last_name", "books_auther"."email" FROM "books_auther" INNER JOIN "books_book_authors" ON ( "books_auther"."id" = "books_book_authors"."auther_id" ) WHERE "books_book_authors"."book_id" = %s' - PARAMS = (5,); args=(5,)
  (0.001) QUERY = 'SELECT "books_auther"."id", "books_auther"."first_name", "books_auther"."last_name", "books_auther"."email" FROM "books_auther" INNER JOIN "books_book_authors" ON ( "books_auther"."id" = "books_book_authors"."auther_id" ) WHERE "books_book_authors"."book_id" = %s' - PARAMS = (6,); args=(6,)
  (0.000) QUERY = 'SELECT "books_auther"."id", "books_auther"."first_name", "books_auther"."last_name", "books_auther"."email" FROM "books_auther" INNER JOIN "books_book_authors" ON ( "books_auther"."id" = "books_book_authors"."auther_id" ) WHERE "books_book_authors"."book_id" = %s' - PARAMS = (7,); args=(7,)
  ```

- 使用prefetch_related()，进行优化，依旧是通过Book查找每本书的作者，但是只访问了数据库两次

  ```python
  def get_book_authors(request):
      """
      获取每本书的作者, 优化版
      """
      books = models.Book.objects.all().prefetch_related('authors')
  
      book_list = []
      for book in books:
          book_info = {}
          book_info['book'] = book.title
          book_info['authors'] = [author.first_name for author in book.authors.all()]
          book_list.append(book_info)
  
      return JsonResponse(book_list, safe=False)
  ```

  ```sqlite
  (0.004) QUERY = 'SELECT "books_book"."id", "books_book"."title", "books_book"."publisher_id", "books_book"."publication_date" FROM "books_book"' - PARAMS = (); args=()
  (0.001) QUERY = 'SELECT ("books_book_authors"."book_id") AS "_prefetch_related_val_book_id", "books_auther"."id", "books_auther"."first_name", "books_auther"."last_name", "books_auther"."email" FROM "books_auther" INNER JOIN "books_book_authors" ON ( "books_auther"."id" = "books_book_authors"."auther_id" ) WHERE "books_book_authors"."book_id" IN (%s, %s, %s, %s, %s)' - PARAMS = (3, 4, 5, 6, 7); args=(3, 4, 5, 6, 7)
  
  ```

### prefetch_related 总结

1. prefetch_related主要针对多对多和多对一关系进行优化。
2. prefetch_related通过分别获取各个表的内容，然后用Python处理他们之间的关系来进行优化。



## 小结

- 主要优化方式还是通过尽可能的减少查询数据库的次数。

