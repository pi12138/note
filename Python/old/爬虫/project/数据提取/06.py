'''
Element.get() 获得属性值
root.getchildren()获得直接子元素
'''

from lxml import etree

def parse():
    # 获取ElementTree
    tree = etree.parse("test01.xml")
    # print(tree)
    # 获取根元素
    root = tree.getroot()
    print(root)
    # 获得root节点name属性值
    print("root.name:", root.get("name"))

    child = root.getchildren()
    print(child)
    print("===" * 10)
    for i in child:
        print('tag:{0}, attrib:{1}, text:{2}'.format(i.tag, i.attrib, i.text))
    



if __name__ == "__main__":
    parse()