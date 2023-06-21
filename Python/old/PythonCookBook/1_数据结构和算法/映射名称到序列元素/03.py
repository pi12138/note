'''
讨论
命名元组另一个用途就是作为字典的替代，因为字典存储需要更多的内存空间。如
果你需要构建一个非常大的包含字典的数据结构，那么使用命名元组会更加高效。但是
需要注意的是，不像字典那样，一个命名元组是不可更改的。比如：

'''
from collections import namedtuple

stu = namedtuple('Student', ['name','age','sex'])
s1 = stu('zyp','20','man')

print("s1:",s1)

# 命名元组内的值不能直接赋值更改
# s1.age = 19       # 会报错
# print(s1.age)

'''
如果你真的需要改变属性的值，那么可以使用命名元组实例的 _replace() 方法，
它会创建一个全新的命名元组并将对应的字段用新的值取代。比如：
'''
s1 = s1._replace(age = 19)
print("s1:", s1)

'''
_replace() 方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字
段时候，它是一个非常方便的填充数据的方法。你可以先创建一个包含缺省值的原型元
组，然后使用 _replace() 方法创建新的值被更新过的实例。比如：
'''
s2 = stu('',0,None)
print("s2:",s2)
s2 = s2._replace(name = 'gzy', age = '22', sex = 'man')
print("s2:", s2)

stu2 = namedtuple('Student',['name','age','sex','id','fraction'])
s3 = stu2('',0,None,0,0)

def dict_to_namedtuple(s):
    return s3._replace(**s)

dict1 = {'name':'zyp','age':20,'sex':'man','id':1615925256,'fraction':100}
print(dict_to_namedtuple(dict1))

dict2 = {'name':'zyp','sex':'man','fraction':100}
print(dict_to_namedtuple(dict2))

'''
最后要说的是，如果你的目标是定义一个需要更新很多实例属性的高效数据结构，
那么命名元组并不是你的最佳选择。这时候你应该考虑定义一个包含 __slots__ 方法
的类（参考 8.4 小节）
'''