'''
问题
你想在字符串中搜索和匹配指定的文本模式
解决方案
对于简单的字面模式，直接使用 str.replace() 方法即可，比如：
'''

text = 'yeah, but no, but yeah, but no, but yeah'

new_text = text.replace('yeah', '耶')
print(text)
print(new_text)

