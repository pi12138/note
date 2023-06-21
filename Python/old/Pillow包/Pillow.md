# Pillow 
	- pillow是PIL的兼容版本，支持最新的python3.x
	- PIL仅支持到python2.7
	
	- 安装：
		- pip install pillow

# Image类
	- Python Imaging Library中最重要的类是 Image类，它在模块中定义，具有相同的名称。您可以通过多种方式创建此类的实例; 通过从文件加载图像，处理其他图像或从头开始创建图像。

	- 要从文件加载图像，请使用模块中的open()函数Image：
		>>> from PIL import Image
		>>> im = Image.open("hopper.ppm")
	- 如果成功，则此函数返回一个Image对象。

	- 获得Image类的实例后，可以使用此类定义的方法来处理和操作图像。例如，让我们显示刚刚加载的图像：
		>>> im.show()

	- 案例见01.py

	- 打开文件：Image.open(filename)
	- 使用外部应用程序显示图片：image_object.show()
	- 保存文件：image_object.save()

	- 转换文件格式，案例见02.py
	- 创建jpeg缩略图，案例见03.py
	- 识别图像文件，案例04.py


	- 剪切一块矩形：image_object.crop()
	- 粘贴：image_object.paste()
	- 剪切、粘贴、合并图像，案例05.py


# 实例1：生成验证码图片，test01.py
