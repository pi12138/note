# `Item Pipeline`

- ![pipeline1](../image/pipeline1.png)



- ![pipeline2](../image/pipeline2.png)

## 如何让pipeline处理不同的item内容

- 两种方式
  - `yield` 返回 `item` 字段时，多添加一个 `item['come_from']` 字段
  - 使用爬虫名判断， `spider.name`
- ![pipeline3](../image/pipeline3.png)

## `Pipeline深入使用`

- ![pipeline4](../image/pipeline4.png)