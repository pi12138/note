"""列表类型不同操作的时间复杂度"""

import timeit


# 测试几种不同方式生成列表所耗费的时间
def test1():
    list1 = []
    for i in range(1, 11):
        list1.append(i)
    # print("test1_list1:", list1)


def test2():
    list1 = [i for i in range(1, 11)]
    # print("test2_list1:", list1)


def test3():
    list1 = list(range(1, 11))


def test4():
    list1 = []
    for i in range(1, 11):
        list1 = list1 + [i]


def test5():
    list1 = []
    for i in range(1, 11):
        list1.extend([i])


if __name__ == '__main__':
    print("append():", timeit.timeit(test1))
    print("列表生成式:", timeit.timeit(test2))
    print("list():", timeit.timeit(test3))
    print("+ :", timeit.timeit(test4))
    print("extend():", timeit.timeit(test5))