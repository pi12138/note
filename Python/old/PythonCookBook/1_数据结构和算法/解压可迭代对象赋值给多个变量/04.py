'''
星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
有时候，你想解压一些元素后丢弃它们，你不能简单就使用 * ，但是你可以使用一
个普通的废弃名称，比如 *_ 或者 *ign （ignore）。

'''

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

line = line.split(':')

name,*str1,path1,path2 = line
print('name:',name)
print('str1:',str1)
print("path1:",path1)
print('path2:',path2)

str1 = 'hello'
head,*tail = str1
print(head)
print(tail)