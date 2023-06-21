# `CrawlSpiders`

- **`class scrapy.spiders.CrawlSpider`**

>>- 通过下面的命令可以快速创建 `CrawlSpider`模板 的代码：
>>  - **`scrapy genspider -t crawl tencent "tencent.com"`**
>>- 它是Spider的派生类，Spider类的设计原则是只爬取`start_url`列表中的网页，而`CrawlSpider`类定义了一些规则(rule)来提供跟进link的方便的机制，从爬取的网页中获取link并继续爬取的工作更适合。

- `CrawlSpider`继承于Spider类，除了继承过来的属性外（name、allow_domains），还提供了新的属性和方法:
- 注意点：
  - 提取到的url地址不完整时，crawlspider会自动补充完整之后，再请求
  - parse（）方法不能定义，它有特殊功能，crawlspider已经实现

## `LinkExtractors`

- **`class scrapy.linkextractors.LinkExtractor`**

- Link Extractors 的目的很简单: 提取链接｡

  每个`LinkExtractor`有唯一的公共方法是 **extract_links()**，它接收一个 Response 对象，并返回一个 `scrapy.link.Link` 对象。

  Link Extractors要实例化一次，并且 extract_links 方法会根据不同的 response 调用多次提取链接｡

  ```python```

  ```python
  class scrapy.linkextractors.LinkExtractor(
      allow = (),
      deny = (),
      allow_domains = (),
      deny_domains = (),
      deny_extensions = None,
      restrict_xpaths = (),
      tags = ('a','area'),
      attrs = ('href'),
      canonicalize = True,
      unique = True,
      process_value = None
  )
  ```

- 主要参数：

  - `allow`：满足括号中“正则表达式”的值会被提取，如果为空，则全部匹配。
  - `deny`：与这个正则表达式(或正则表达式列表)不匹配的URL一定不提取。
  - `allow_domains`：会被提取的链接的domains。
  - `deny_domains`：一定不会被提取链接的domains。
  - `restrict_xpaths`：使用`xpath`表达式，和allow共同作用过滤链接。

  - **使用示例：糗事百科**

  ```python
  >>> scrapy shell -s USER_AGENT='Mozilla/5.0'
  >>> fetch("https://www.qiushibaike.com/text/")
  >>> from scrapy.linkextractors import LinkExtractor
  >>> link_list = LinkExtractor(allow=("/text/page/\d+/"))
  >>> link_list.extract_links(response)
  [Link(url='https://www.qiushibaike.com/text/page/2/', text='\n\n\n2\n\n', fragment='', nofollow=True), Link(url='https://www.qiushibaike
  .com/text/page/3/', text='\n\n\n3\n\n', fragment='', nofollow=True), Link(url='https://www.qiushibaike.com/text/page/4/', text='\n\n\n4\
  n\n', fragment='', nofollow=True), Link(url='https://www.qiushibaike.com/text/page/5/', text='\n\n\n5\n\n', fragment='', nofollow=True),
   Link(url='https://www.qiushibaike.com/text/page/13/', text='\n\n\n13\n\n', fragment='', nofollow=True)]
  
  
  ```

## rules

- **在rules中包含一个或多个Rule对象，每个Rule对爬取网站的动作定义了特定操作**。如果多个rule匹配了相同的链接，则根据规则在本集合中被定义的顺序，第一个会被使用。

  ```python
  class scrapy.spiders.Rule(
          link_extractor, 
          callback = None, 
          cb_kwargs = None, 
          follow = None, 
          process_links = None, 
          process_request = None
  )
  ```

- `link_extractor`：是一个Link Extractor对象，用于定义需要提取的链接。

- `callback`： 从link_extractor中每获取到链接时，参数所指定的值作为回调函数，该回调函数接受一个response作为其第一个参数。

  > - **注意**：当编写爬虫规则时，避免使用parse作为回调函数。由于CrawlSpider使用parse方法来实现其逻辑，如果覆盖了 parse方法，crawl spider将会运行失败。

- `follow`：是一个布尔(boolean)值，指定了根据该规则从response提取的链接是否需要跟进。 如果callback为None，follow 默认设置为True ，否则默认为False。

- `process_links`：指定该spider中哪个的函数将会被调用，从link_extractor中获取到链接列表时将会调用该函数。该方法主要用来过滤。也可以用来处理链接。

- `process_request`：指定该spider中哪个的函数将会被调用， 该规则提取到每个request时都会调用该函数。 (用来过滤request)

- **rules中可以包含一个或多个Rule对象**

  ```python
  rules = (
          Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
      )
  
  ```

  