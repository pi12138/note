# Scrapy下载图片内容

- Scrapy 提供了一种图片下载和存储的方式
- 利用`ImagesPipeline`下载图片

##  ImagesPipeline简介

- Scrapy用ImagesPipeline类提供一种方便的方式来下载和存储图片。
- 特点：
  - 将下载图片转换成通用的JPG和RGB格式
  - 避免重复下载
  - 缩略图生成
  - 图片大小过滤

## ImagesPipeline工作流程

- 当使用图片管道 ImagePipeline,典型的工作流程如下:
  - 在一个爬虫里,你抓取一个项目,把其中图片的URL放入image_urls组内。
  - 项目从爬虫内返回,进入项目管道。
  - 当项目进入ImagePipeline, image_urls组内的URLs将被Scrapy的调度器和下载器安排下载(这意味着调度器和中间件可以复用),当优先级更高,会在其他页面被抓取前处理. 项目会在这个特定的管道阶段保持”locker”的状态,直到完成图片的下载(或者由于某些原因未完成下载)。
  - 当图片下载完, 另一个组(images)将被更新到结构中,这个组将包含一个字典列表,其中包括下载图片的信息,比如下载路径,源抓取地址(从image_urls组获得)和图片的校验码. images列表中的图片顺序将和源image_urls组保持一致.如果某个图片下载失败,将会记录下错误信息,图片也不会出现在images组中。

## 示例

- `pipelines.py`自定义ImagesPipeline代码

```python
    import scrapy
    import os
    from scrapy.pipelines.images import ImagesPipeline
    from scrapy.utils.project import get_project_settings

    
    class DouyuPipeline(ImagesPipeline):
        # 获取settings文件中的常量
        IMAGE_STORE = get_project_settings().get("IMAGES_STORE")

        def get_media_requests(self, item, info):
            image_url = item['image_url']

            yield scrapy.Request(image_url)

        def item_completed(self, results, item, info):
            # 固定写法，获取图片路径，同时判断这个路径是否正确，如果正确，则放入 image_path 里
            image_path = [x['path'] for ok, x in results if ok]

            os.rename(self.IMAGE_STORE+image_path[0], self.IMAGE_STORE+item['name']+'.jpg')
            item['image_path'] = self.IMAGE_STORE + item['name']

            return item

        # get_media_requests的作用就是为每一个图片链接生成一个Request对象，
        # 这个方法的输出将作为item_completed的输入中的results，
        # result是一个包含tuple的容器,容器中每个元组包含两个值，每个元组包括(success, image_info_or_failure)。
        # 如果success=true，image_info_or_failure是一个字典，包括url/path/checksum三个key。
```



- `settings.py`设置图片下载位置

- **注意：因为使用的是框架自带的下载图片的方式，所以图片存储位置的命名必须和框架要求一致为"IMAGES_STORE"**

- 如果不一致则不会进行图片下载

  ```python
  # 图片存储位置,该变量名固定必须为"IMAGES_STORE"
  IMAGES_STORE = "./download_images/"
  
  ```

### 注意

- `image_path = [x['path'] for ok, x in result if ok]`

- 列表生成式,上面是将results的值分别给x,ok,如果ok的值为True,那么就取x['path']最后形成一个一个list

- ```python
  for ok,x in result:
      if ok:
          iamge_path = [x['path']]
  ```



