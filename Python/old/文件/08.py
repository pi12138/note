# shelve 使用案例

import shelve
# 使用shelve存储数据
# help(shelve.open)

# 
shv = shelve.open(r'./test01.db')
# print(type(shv))
shv['name'] = 'zyp'
shv['age'] = 20
shv['address'] = '信阳'

shv.close()
# 通过以上案例发现
# shelve自动创建的不仅仅是test01.db一个文件，还包括其他数据库文件

# 读取数据
shv = shelve.open(r'./test01.db')

print(shv)
print(shv['name'])
print(shv['age'])
print(shv['address'])
shv.close()