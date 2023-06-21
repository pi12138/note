# coding:utf-8


def quick_sort(alist, start, end):
    """快速排序"""
    # 递归的退出条件
    if start >= end:
        return

    low = start
    high = end
    middle_value = alist[start]

    # 排序主要算法
    while low < high:
        # high移动
        while low < high and alist[high] >= middle_value:
            high -= 1
        # 当alist[high] < middle_value时跳出循环，将high位置的值放到low位置上
        alist[low] = alist[high]

        # low移动
        while low < high and alist[low] < middle_value:
            low += 1
        # 当alist[low] >= middle_value时跳出循环，将low位置上的值放到high位置上
        alist[high] = alist[low]
    # 当low = high时跳出循环，将中间值middle_value放到low或者high位置上
    alist[low] = middle_value
    # 上面代码执行一次后，middle_value左边的值全部小于middle_value, 右边的值全部大于middle_value

    # middle_value左边数列再次递归
    quick_sort(alist, start, low-1)
    # middle_value右边的数列再次递归
    quick_sort(alist, low+1, end)


if __name__ == "__main__":
    list2 = [55, 66, 77, 33, 22, 44, 88, 66]
    print(list2)
    quick_sort(list2, 0, len(list2)-1)
    print(list2)