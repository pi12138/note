# coding:utf-8


def select_sort(list):
    """选择排序"""
    n = len(list)

    for i in range(0, n-1):
        # min_index用来记录最小值位置
        min_index = i
        for j in range(i+1, n):
            if list[min_index] > list[j]:
                min_index = j
        if min_index != i:
            list[i], list[min_index] = list[min_index], list[i]


if __name__ == "__main__":
    list1 = [55, 66, 77, 33, 22, 44, 88]
    print(list1)
    select_sort(list1)
    print(list1)