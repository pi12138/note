import xml.dom.minidom

# 负责解析xml文件
from xml.dom.minidom import parse

# 使用minidom打开xml文件
DOMTree = xml.dom.minidom.parse("student.xml")

# 得到文档对象
doc = DOMTree.documentElement

# 显示子元素
for ele in doc.childNodes:
	if ele.nodeName == "Teacher":
		print("-------Name:{0}-------".format(ele.nodeName))
		childs = ele.childNodes
		# for child in childs:
		# 	print(child.nodeName)
		for child in childs:
			if child.nodeName == "name":
				# data是文本结点的第一个属性，表示他的值
				print("Name:{0}".format(child.childNodes[0].data))
			if child.nodeName == "mobile":
				# data是文本结点的第一个属性，表示他的值
				print("Mobile:{0}".format(child.childNodes[0].data))
			if child.nodeName == "age":
				# data是文本结点的第一个属性，表示他的值
				print("Age:{0}".format(child.childNodes[0].data))
				if child.hasAttribute("Detail"):
					print("Age-detail:{0}".format(child.getAttribute("Detail")))
	if ele.nodeName == "student":
		print("-------Name:{0}-------".format(ele.nodeName))
		childs = ele.childNodes
		# for child in childs:
		# 	print(child.nodeName)
		for child in childs:
			if child.nodeName == "name":
				# data是文本结点的第一个属性，表示他的值
				print("Name:{0}".format(child.childNodes[0].data))
			if child.nodeName == "mobile":
				# data是文本结点的第一个属性，表示他的值
				print("Mobile:{0}".format(child.childNodes[0].data))
			if child.nodeName == "age":
				# data是文本结点的第一个属性，表示他的值
				print("Age:{0}".format(child.childNodes[0].data))
				if child.hasAttribute("Detail"):
					print("Age-detail:{0}".format(child.getAttribute("Detail")))
