# `Scrapy_redis分布式爬虫编写`

## `settings`文件中需要添加部分内容

```python
# 指定哪个去重方法给request对象去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 指定scheduler队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 队列中内容是否持久保存，为false时关闭redis会清空redis
SCHEDULER_PERSIST = True

# scrapy_redis实现的items保存到redis的pipeline
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# 指定的redis地址， 也可以这样写 REDIS_URL = "redis://127.0.0.1:6379"
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
# 如果redis没有密码可以不用设置
REDIS_PARAMS = {
    'password': 'root',
}
```



## `spider需要改写`

```python
# 官方示例案例
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider


# 继承类需要修改
class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    # 爬虫名
    name = 'mycrawler_redis'
    # 指定redis中 start_urls 的键
    # 启动的时候只需要对应的键存入url地址，不同位置的爬虫会获取该url地址
    # 启动步骤一般分两步
    # 1. Slaver端输入 "scrapy crawl myspider_redis"(或者 "scrapy runspider myspider_redis"), 让爬虫就绪
    # 2. Master端往redis数据库中写入 `lpush myspider:start_urls "http://xxxxx"` 让Slaver端的每个爬虫从这个url开始爬取
    redis_key = 'mycrawler:start_urls'
    # 手动指定allow_domain
	allow_domain = ["dmoztools.net"]
    
    rules = (
        # follow all links
        Rule(LinkExtractor(), callback='parse_page', follow=True),
    )

    # 动态设置 allow_domain, 一般不需要直接手动指定即可
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MyCrawler, self).__init__(*args, **kwargs)

    def parse_page(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }

```

## 运行爬虫

- 启动步骤一般分两步
  -  Slaver端输入 "scrapy crawl myspider_redis"(或者 "scrapy runspider myspider_redis"), 让爬虫就绪
  - Master端往redis数据库中写入 `lpush myspider:start_urls "http://xxxxx"` 让Slaver端的每个爬虫从这个url开始爬取



## 案例

- [当当图书爬虫](https://blog.csdn.net/weixin_43182689/article/details/89470623)