'''
问题
你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的
代码难以阅读，于是你想通过名称来访问元素。

解决方案
collections.namedtuple() 函数通过使用一个普通的元组对象来帮你解决这个问
题。这个函数实际上是一个返回 Python 中标准元组类型子类的一个工厂方法。你需要
传递一个类型名和你需要的字段给它，然后它就会返回一个类，你可以初始化这个类，
为你定义的字段传递值等。代码示例：
'''
from collections import namedtuple

info1 = namedtuple('info_zyp', ['sex','height', 'weight'])
zyp = info1('man', '180cm', '70kg')
print(zyp)
print("sex:", zyp.sex)
print("height:", zyp.height)
print("weight:", zyp.weight)

'''
尽管 namedtuple 的实例看起来像一个普通的类实例，但是它跟元组类型是可交换
的，支持所有的普通元组操作，比如索引和解压。比如：
'''
print("len(zyp):", len(zyp))
xinbie,shengao,tizhong = zyp
print("xinbie:", xinbie)
print("shengao:",shengao)
print("tizhong:",tizhong)
