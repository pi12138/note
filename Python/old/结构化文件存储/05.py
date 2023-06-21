import xml.dom.minidom as dm
# 在内存中创建一个空的文档
doc = dm.Document()
# 创建一个根节点School对象
root = doc.createElement("School")
# 添加根节点属性
root.setAttribute('name', 'nyist')
root.setAttribute('address', 'nanyang')
# help(root.setAttribute)
# setAttribute(attname, value)
# 将根节点添加到文档对象中
doc.appendChild(root)

information_list = [{'name':'zyp', 'age':'20', 'sex':'man'}, {'name':'gyj', 'age':'20', 'sex':'man'}, {'name':'kah', 'age':'21', 'sex':'man'}]

for i in information_list:
	nodeperson = doc.createElement("person")
	# 给叶子节点name设置一个文本节点，用于显示文本内容
	nodename = doc.createElement("name")
	nodename.appendChild(doc.createTextNode(str(i['name'])))

	nodeage = doc.createElement("age")
	nodeage.appendChild(doc.createTextNode(str(i['age'])))

	nodesex = doc.createElement("sex")
	nodesex.appendChild(doc.createTextNode(str(i['sex'])))

	#将各叶子节点添加到父节点Manager中，
    #最后将Manager添加到根节点Managers中
	nodeperson.appendChild(nodename)
	nodeperson.appendChild(nodeage)
	nodeperson.appendChild(nodesex)
	root.appendChild(nodeperson)
# 开始写xml文档
fp = open('School.xml', 'w')
doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")