'''
解析xml文件
'''

from lxml import etree

def parse():
    # 获取ElementTree
    tree = etree.parse("test01.xml")
    # print(tree)
    # 获取根元素
    root = tree.getroot()
    print(root)
    # get(attrib)可以获得指定属性值
    print("root.name:", root.get("name"))
    print("root.tag:{0}, root.attrib:{1}, root.text:{2}".format(root.tag, root.attrib, root.text))
    # 迭代获取子元素
    for child in root:
        print("child.tag:{0}, child.attrib:{1}, child.text:{2}".format(child.tag, child.attrib, child.text))
        for child_child in child:
            print("child_child.tag:{0}, child_child.attrib:{1}, child_child.text:{2}".format(child_child.tag, child_child.attrib, child_child.text))



if __name__ == "__main__":
    parse()