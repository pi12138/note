from __future__ import print_function
from PIL import Image
# 创建一个Image对象
image1 = Image.open('1.jpeg')

# 展示
# image1.show()

# 使用实例属性检查文件内容
print(image1.format, image1.size, image1.mode)