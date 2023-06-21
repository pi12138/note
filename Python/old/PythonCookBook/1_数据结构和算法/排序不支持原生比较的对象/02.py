'''
另外一种方式是使用 operator.attrgetter() 来代替 lambda 函数：

讨论
选择使 用 lambda 函数或者 是 attrgetter() 可能取决 于个人 喜好。但是，
attrgetter() 函数通常会运行的快点，并且还能同时允许多个字段进行比较。这
个跟 operator.itemgetter() 函数作用于字典类型很类似（参考 1.13 小节）。例如，
如果 User 实例还有一个 first_name 和 last_name 属性，那么可以向下面这样排序：
by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
'''
from operator import attrgetter

class User():
    def __init__(self, id, name):
        self.user_id = id
        self.user_name = name
    
    def __repr__(self):
        return 'User({0}, {1})'.format(self.user_id, self.user_name)

def sort_notcompare():
    user = [User(99, 'zyp'), User(3, 'gyj'), User(20, 'gzy'), User(99, 'zy')]
    print(user)
    # sort_user = sorted(user, key=lambda u: u.user_id)
    sort_user = sorted(user, key = attrgetter('user_id','user_name'))
    print(sort_user)
    # 同样需要注意的是，这一小节用到的技术同样适用于像 min() 和 max() 之类的函
    # 数。比如：
    min_user = min(user, key = attrgetter('user_id'))
    max_user = max(user, key = attrgetter('user_id'))
    print(min_user)
    print(max_user)

sort_notcompare()



