'''
find(),findall(),iterfind()的使用
'''

from lxml import etree

def parse():
    tree = etree.parse('test01.xml')
    root = tree.find('teacher')
    root_list = tree.findall("teacher")
    root_iter = tree.iterfind('student')
    
    print(root)
    print(root.attrib)

    print(root_list)
    for i in root_list:
        print(i.attrib)

    print(root_iter)
    for i in root_iter:
        print(i.attrib)

    

if __name__ == "__main__":
    parse()