# os模块和sys模块

## 区别

- os  模块是与操作系统相关的
- sys 模块是与python系统相关的

## os 模块一般会用到的操作

- 判断文件夹是否存在，如果不存在则创建一个文件夹

```python

import os

if os.path.exists(FloderPath):
	pass
else:
	os.mkdir(FloderPath)

```

- `os.path.realpath(__file__)`返回当前文件的绝对路径
- `os.path.dirname(file)` 返回当前文件所在的文件目录

## sys模块的一些操作

- 获取Python对象占用的内存空间的大小
	- sys.getsizeof(obj [,default])
