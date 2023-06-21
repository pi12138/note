# Scrapy项目基本步骤

## 一、新建项目

- `scrapy startproject project_name`

## 二、明确目标

- 在 `project_name/items.py` 文件中构建 item 模型
- 设置好需要保存的数据字段

## 三、制作爬虫

### 1. 爬数据

- 在 `project_name` 下执行 `scrapy genspider spider_name "website_domain"` 

- 将会在 `project_name/spider` 目录下创建一个名为 `spider_name.py` 的爬虫文件

- `spider_name.py` 文件默认内容

  ```python
  import scrapy
  
  class Spider_nameSpider(scrapy.Spider):
      name = "spider_name"
      allowed_domains = ["website_domain"]
  	start_urls = ["http://xxxxxx"]
      def parse(self, response):
          pass
  ```

- 也可以在 `project_name/spider` 目录下自行创建这个文件

- 要建立一个Spider， 你必须用scrapy.Spider类创建一个子类，并确定了三个强制的属性 和 一个方法。

  - `name = ""` ：这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。
  - `allow_domains = []` 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。
  - `start_urls = ()` ：**爬取的URL元祖/列表。**爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。
  - `parse(self, response)` ：解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下：
    1. 负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
    2. 生成需要下一页的URL请求。

- 执行爬虫`scrapy crawl itcast`

### 2. 取数据

- 将 `project_name/items.py` 中定义的 `item模型类` 引入到 `spider_name.py` 文件中
- 然后新建一个 `item模型对象` 然后可以使用该模型对象保存内容
- 最后return返回一个模型对象，或者模型对象列表
- 最后也可以使用 `yield` 逐个返回模型对象
  - 该种返回数据的方式需要编写pipelines管道文件
    1. 在`settings.py` 文件中开启 `ITEM_PIPELINES`， 并且设置好需要使用的管道类
    2. 然后在`pipelines.py` 中编写该管道文件
    3. 该文件中需要编写管道类，每个管道类必须要有一个`process_item(self, item, spider)` 函数，该函数会在管道类使用时被调用
    4. 在该`process_item`函数中编写需要的操作
  - 推荐使用该种方式取数据

## 四、执行爬虫

-  `scrapy crawl itcast`

- ##### scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，，命令如下：

  ```python
  # json格式，默认为Unicode编码
  scrapy crawl itcast -o teachers.json
  
  # json lines格式，默认为Unicode编码
  scrapy crawl itcast -o teachers.jsonl
  
  # csv 逗号表达式，可用Excel打开
  scrapy crawl itcast -o teachers.csv
  
  # xml格式
  scrapy crawl itcast -o teachers.xml
  
  ```

## 五、再次发送请求

- 将新的请求发送给 调度器入队列，出队列，在交给下载器下载
- `yield scrapy.Request(url, callback=self.parse)`