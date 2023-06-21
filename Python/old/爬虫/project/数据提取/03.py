'''
读取xml文件
etree只能读取xml文件，读取html文件会报错
test02.htmlh和test03.html的区别是，前者是标准格式的html文件，后者只有简单的标签
'''

from lxml import etree

if __name__ == "__main__":
    xml = etree.parse('test01.xml')
    # html = etree.parse('test02.html')# 报错
    html = etree.parse('test03.html') 

    content1 = etree.tostring(xml)
    content2 = etree.tostring(xml, pretty_print = True)
    # content3 = etree.tostring(html)
    html_data = html.xpath('//*')
    print(content1)
    print(content2)
    # print(content3)
    for i in html_data:
        print(i.text)