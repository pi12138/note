'''
问题
你想排序类型相同的对象，但是他们不支持原生的比较操作。

解决方案
内置的 sorted() 函数有一个关键字参数 key ，可以传入一个 callable 对象给
它，这个 callable 对象对每个传入的对象返回一个值，这个值会被 sorted 用来排序
这些对象。比如，如果你在应用程序里面有一个 User 实例序列，并且你希望通过他们
的 user_id 属性进行排序，你可以提供一个以 User 实例作为输入并输出对应 user_id
值的 callable 对象。比如：
'''

class User():
    def __init__(self, id):
        self.user_id = id
    
    def __repr__(self):
        return 'User({})'.format(self.user_id)

def sort_notcompare():
    user = [User(99), User(3), User(20), User(55)]
    print(user)
    sort_user = sorted(user, key=lambda u: u.user_id)
    print(sort_user)

    
sort_notcompare()