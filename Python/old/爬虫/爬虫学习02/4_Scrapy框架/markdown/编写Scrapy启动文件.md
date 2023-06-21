# 编写scrapy启动文件

```python
# start.py
from scrapy import cmdline
# 将执行命令字符串切片，分别执行
cmdline.execute("scrapy crawl spider_name".split())
```

