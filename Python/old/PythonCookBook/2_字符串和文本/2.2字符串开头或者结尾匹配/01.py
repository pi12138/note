'''
问题
你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URLScheme 等等。

解决方案
检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.endswith() 方法。比如：
'''
filename = 'file.txt'
print(filename.startswith("file"))
print(filename.endswith('.txt'))

url = 'https://www.baidu.com'
print(url.startswith('https:'))

