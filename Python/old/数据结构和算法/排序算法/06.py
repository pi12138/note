# coding:utf-8
# 归并排序在时间复杂度上比其他排序算法小，但是在空间上使用比其他排序算法多。

def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist

    mid = n//2      # 取整
    # 二分分解，将列表分为左右两个部分，同时排序
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    left_pointer, right_pointer = 0, 0

    result = []     # 空链表用来接收排序数据
    # 排序过程,将两个有序的子集并为一个新的有序整体
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] < right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1

    # 当循环退出时，即left_pointer = len(left_list) 或者 right_pointer = len(right_list)
    # 列表下标越界
    # 当列表下标越界切片时，列表会返回空，而不是报错
    # 将剩下的元素放到最后
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]

    return result


if __name__ == "__main__":
    list2 = [55, 66, 77, 33, 22, 44, 88, 66]
    print(list2)
    new_list = merge_sort(list2)
    print(new_list)