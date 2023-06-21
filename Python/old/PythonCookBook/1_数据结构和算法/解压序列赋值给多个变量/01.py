'''
现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值
给 N 个变量？

解决方案
任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多
个变量。唯一的前提就是变量的数量必须跟序列元素的数量是一样的。
如果变量个数和序列元素的个数不匹配，会产生一个异常。

讨论
实际上，这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。
包括字符串，文件对象，迭代器和生成器。
'''


t1 = (1,2,3,4,5)
a,b,c,d,e = t1
print(a,b,c,d,e)

# 变量数量和序列元素数量不一样
try:
    a,b,c,d = t1
    print(a,b,c,d)
except:
    print("error,变量的数量必须跟序列元素的数量是一样")

s1 = 'hello'
a,b,c,d,e = s1
print(a,b,c,d,e)

student = ['zyp', '18', 'man', (1998,11,18)]
name,age,sex,birth = student
print('name:',name)
print('age:',age)
print('sex:',sex)
print('birth:',birth)

year,month,day = birth
print('birth:{0}.{1}.{2}'.format(year,month,day))

