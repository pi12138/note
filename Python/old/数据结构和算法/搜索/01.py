# coding:utf-8

"""
二分查找
    优点：省时间
    缺点：局限性，只能查找有序列表
    01.py 非递归实现
    02.py 递归实现
"""


def binary_search(alist, item):
    first = 0
    last = len(alist) - 1

    while first <= last:
        middle = (first + last) // 2
        if alist[middle] == item:
            print(middle)
            return True
        elif alist[middle] > item:
            last = middle - 1
        elif alist[middle] < item:
            first = middle + 1
    # first > last
    return False


if __name__ == "__main__":
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search(testlist, 3))
    print(binary_search(testlist, 13))
    print(binary_search(testlist, 17))