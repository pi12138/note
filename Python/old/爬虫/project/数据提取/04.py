'''
etree和xpath的联合使用

'''
from lxml import etree

if __name__ == "__main__":
    xml = etree.parse('test01.xml')
    # print(type(xml))
    # print(dir(xml))
    xml_data1 = xml.xpath('//school')               # 查找school节点
    xml_data2 = xml.xpath('//student[@number]')     # 查找有number属性的student节点
    xml_data3 = xml.xpath('//student[@number]/*')   # 查找有number属性的student节点下的所有子节点

    print(type(xml_data1))
    # print(dir(xml_data1))
    print(xml_data1)
    # for i in xml_data:
        # print(i.text)
    # 列表内只有一条内容,可以直接使用下标打印
    print(xml_data1[0].tag) 
    print("===" * 10)

    print(type(xml_data2))
    print(xml_data2)
    for i in xml_data2:
        print(i.tag)
        print(i.attrib)
        print(i.text)
        for child in i:
            print(child.tag, child.attrib, i.text)
    print("===" * 10)
    
    print(type(xml_data3))
    print(xml_data3)
    for i in xml_data3:
        print(i.tag)
        print(i.attrib)
        print(i.text)
