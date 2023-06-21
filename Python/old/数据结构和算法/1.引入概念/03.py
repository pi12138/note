"""
测试列表两种不同的插入方式的时间复杂度
1. list.append()
2. list.insert()
"""

import timeit


def test1():
    l1 = []
    for i in range(1, 10000):
        l1.append(i)


def test2():
    # 从尾部添加
    l1 = []
    for i in range(1, 10000):
        l1.insert(i-1, i)


def test3():
    # 从头部添加
    l1 = []
    for i in range(1, 10000):
        l1.insert(0, i)


if __name__ == '__main__':
    timeit1 = timeit.Timer("test1()", "from __main__ import test1")
    timeit2 = timeit.Timer("test2()", "from __main__ import test2")
    timeit3 = timeit.Timer("test3()", "from __main__ import test3")
    print("append():", timeit1.timeit(1000))
    print("insert(i-1):", timeit2.timeit(1000))
    print("insert(0):", timeit3.timeit(1000))
