'''
问题
你想匹配或者搜索特定模式的文本

解决方案
如果你想匹配的是字面字符串，那么你通常只需要调用基本字符串方法就行，比如
str.find() , str.endswith() , str.startswith() 或者类似的方法：
'''
text = 'yeah, but no, but yeah, but no, but yeah'

print(text.startswith('yeah'))
print(text.endswith('but yeah'))
print(text[10])
print(text[28])
print(text.find('no'))      # 查找不到指定内容返回-1

# 可以查找整个字符串的所有指定字段
def find_all(str, find_str):
    pos = []
    pos1 = str.find(find_str)
    while pos1 != -1:
        # print(pos1)
        pos.append(pos1)
        pos1 = str.find(find_str, pos1+1)
    return pos

print(find_all(text, 'no'))
         
