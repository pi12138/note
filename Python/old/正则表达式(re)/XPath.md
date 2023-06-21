	- https://blog.csdn.net/qq_36148847/article/details/79167267

# 1. XPath
	- 在xml文件中查找信息的一套规则/语言，根据xml的元素或者属性进行遍历

# 2. 选取结点
	- nodename：选取此节点的所有的子节点
	- /：从根节点开始选取
	- //：选取节点不考虑位置
	- .：选取当前节点
	- ../：选取当前节点的父亲节点
	- @：选取属性
	- XPath中查找一般按照路径方法查找，以下是路径表示方法
		'''
			school/teacher:返回teacher节点
			school/student:返回student节点

			//student：选取student节点不考虑位置
			school//age：选取school后代age的所有节点
			//@other：选取other属性
			//age[@detail]:选取带有属性detail的age节点
		'''

# 3.谓语-predicates
	- /school/student[1]：选取school下面的第一个student节点
	- /school/student[last()]:选取school下面的student最后一个节点
	- /school/student[last()-1]:选取school下面student倒数第二个节点
	- /school/student[position()<3]:选取school下面student的前两个节点
	- //student[@score]:选取带有属性score的student节点
	- //student[@score = "99"]：选取带有属性score并且属性score为99的student节点
	- //student[@score]/age：选取带有属性score的student节点的子节点age

# xpath的一些操作
	- |：计算两个节点集
			//student[@score]|//teacher:选取带有属性score的student节点和teacher节点

