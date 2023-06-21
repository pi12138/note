'''
etree 使用示例

'''

from lxml import etree

text = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div>
        <h1>这是第一个标题</h1>
        <p>这是第一段内容</p>
    </div>
    <div>
        <h1>这是第二个标题</h1>
        <p>这是第二段内容</p>
    </div>

</html>
'''
html = etree.HTML(text)
# etree可以自动补全代码
# 上述代码少了一个</body>
s = etree.tostring(html)    

print(html)
# print(s)
print(html.text)
s = s.decode()
print(s)