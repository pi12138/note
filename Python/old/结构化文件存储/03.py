# 对文件内容进行更改
import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse(r"edit.xml")

root = tree.getroot()

for e in root.iter("Name"):
	print(e.tag, ":" ,e.text)

for e in root.iter("Student"):
	# print(e.tag, ":", e.text)
	name = e.find("Name")
	# print(type(name))
	# print(name.text)
	if name.tag != None:
		# print("{0}:{1}".format(name.tag, name.text))
		name.set('test', name.text * 2)
		# help(name.set)
		# help(name.append)
		# help(name.remove)

stu = root.find("Student")
# 生成一个新的元素
e = xml.etree.ElementTree.Element("NewElement")
e.attrib = {'a':'b'}
e.text = "new_add"
stu.append(e)

# 一定要把修改后的内容写回文件，否则修改无效
tree.write("edit.xml")	