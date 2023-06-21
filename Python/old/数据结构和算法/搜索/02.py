# coding:utf-8


def binary_search(alist, item):
    """递归实现二分查找"""
    if len(alist) == 0:
        return False
    else:
        middle = len(alist) // 2
        if alist[middle] == item:
            # print(middle)
            return True
        else:
            if alist[middle] > item:
                return binary_search(alist[:middle], item)
            else:
                return binary_search(alist[middle+1:], item)


if __name__ == "__main__":
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search(testlist, 3))
    print(binary_search(testlist, 13))
    print(binary_search(testlist, 17))
    print(binary_search(testlist, 31))