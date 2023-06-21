'''
root[0][1]根据索引查找子元素
'''

from lxml import etree

def parse():
    tree = etree.parse('test01.xml')
    root = tree.getroot()

    # root[0]是school节点第一个子节点
    print(root[0])
    print(root[0].attrib)
    print(root[0][0])
    


if __name__ == '__main__':
    parse()