# Django上传文件

## request.FILES
	- 一个字典
	- django在文件上传期间，实际文件数据存储在request.FILES中。
	- 这个字典中的每个条目都是一个UploadedFile对象

## class UploadedFIle
	- 常用方法：
		- UploadedFile.read()	读取上传文件的所有数据（到内存），小心使用如果文件过大，会导致内存出现问题
		- UploadedFile.chunks() 	生成器返回文件块，通常配合for循环使用
	
	- 常用属性：
		- UploadedFile.name 	文件名
		- UploadedFile.size 	文件大小
		- UploadedFile.content_type 	文件类型
		- UploadedFile.content_type_extra
		- UploadedFile.charset 	文件字符集

## Django中的FileField和ImageField

- 一般情况下，上传的文件流都不会保存在数据库中，数据库中保存的一般都是文件路径（本地路径或者其他云文件存储路径）
- django中两个模型字段都有一个`upload_to`参数，用来保存文件的路径
- `upload_to`参数使用有三次方式

### 硬编码路径

- 先在项目中的settings文件中设置好`MEDIA_ROOT`和`MEDIA_URL`

- 然后给`upload_to`参数传入一个指定的文件存放前缀路径

- ```python
    # settings.py
    
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    MEDIA_URL = '/media/'
    
    
    # models.py
    
    class User(models.Model):
        image  = models.ImageField(upload_to='images/')
    ```

- 这样指定的文件保存路径就为`MEDIA_ROOT/images/filename`

### 使用strftime()

- 上面一个方式保存的文件可能导致一个文件夹内容过多，甚至某些内容重名
- django在`upload_to`上内置了strftime()函数

- ```python
  	# models.py

	class User(models.Model):
		image = models.ImageField(upload_to='images/%Y/%m/%d/')
  ```

- 这样保存下来的文件路径为`MEDIA/images/年/月/日/`

### 自定义上传路径

- `upload_to`还可以接受一个可调用对象，这个可调用对象必须接受两个参数，instance和filename
- instance 代表该字段说在的模型的实例
- filename 代表最初的文件名

- ```python
	def upload_to(instance, filename):
		return '/'.join([settings.MEDIA_ROOT, instance.other_field, filename])

	class User(models.Model):
		image = models.ImageField(upload_to = upload_to)
		other_filed = models.CharField(max_length=100)
  ```

### 上传文件函数

```python
    def save_file(self, file):
        if not file:
            return {'msg': "未传入文件"}

        try:
            local_file = open('media/design/{}'.format(file.name), 'wb')
            for chunk in file.chunks():
                local_file.write(chunk)
        except Exception as e:
            return {'msg': "保存文件失败", 'error': e}
        finally:
            local_file.close()

        return True
```
