'''
扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设
计的。通常，这些可迭代对象的元素结构有确定的规则（比如第 1 个元素后面都是电
话号码），星号表达式让开发人员可以很容易的利用这些规则来解压出元素来。而不是
通过一些比较复杂的手段去获取这些关联的元素值。
值得注意的是，星号表达式在迭代元素为可变长元组的序列时是很有用的。比如，
下面是一个带有标签的元组序列：

'''

infos = [('zyp','180cm','75kg'),('zy','man')]

def info_body(height, weight):
    
    print('height:',height)
    print('weight:',weight)

def info_sex(info):
    sex = info
    print('sex:',sex)

for arg, *args in infos:
    if arg == 'zyp':
        info_body(*args)
    elif arg == 'zy':
        info_sex(*args)