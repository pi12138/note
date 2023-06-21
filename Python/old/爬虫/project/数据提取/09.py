'''
root.iter()
'''

from lxml import etree

def parse():
    tree = etree.parse('test01.xml')
    root = tree.getroot()

    data = list(root.iter())
    # print(data)
    for i in data:
        print(i)

    print("*" * 50)
    data2 = root.iter('student')
    # print(data2)
    for i in data2:
        print(i)

if __name__ == '__main__':
    parse()