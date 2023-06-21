import xml.etree.ElementTree


root = xml.etree.ElementTree.parse("student.xml")

print("利用getiterator访问：")
nodes = root.getiterator()

for node in nodes:
	print("{0}---{1}".format(node.tag, node.text))

print("*" * 20)
print("利用find方法")
ele_teacher = root.find("Teacher")
# print(type(ele_teacher))
for ele in ele_teacher:
	print("{0}---{1}".format(ele.tag, ele.text))

print("*" * 20)
print("利用findall方法")
ele_student = root.findall("student")
# print(type(ele_student))
for ele in ele_student:			# <student></student>标签
	# print("{0}---{1}".format(ele.tag, ele.text))
	for e in ele.getiterator():				# <student>标签的子标签
		print("{0}---{1}".format(e.tag, e.text))

		if e.tag == "name":
			if "Other" in e.attrib.keys():
				print(e.attrib["Other"])
				# print(e.attrib.keys())



