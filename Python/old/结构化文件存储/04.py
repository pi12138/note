import xml.etree.ElementTree as et

stu = et.Element("Student1")

name = et.SubElement(stu, "Name")
# help(xml.etree.ElementTree.SubElement) 没有解释
name.attrib = {"name":"zyp"}
name.text = "zhou"

age = et.SubElement(stu, "Age")
age.text = "20"		# 必须加引号，不能是int，因为int类型不能迭代

addr = et.SubElement(stu, "Addr")
addr.text = "信阳"

et.dump(stu)