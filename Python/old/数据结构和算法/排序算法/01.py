# coding:utf-8


def bubble_sort(list):
    """冒泡排序"""
    n = len(list)

    for i in range(0, n-1):
        # count的目的是为了处理已经有序的序列，不用进行排序
        count = 0
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                count += 1
        if 0 == count:
            return


if __name__ == "__main__":
    list1 = [55, 66, 77, 33, 22, 44, 88]
    print(list1)
    bubble_sort(list1)
    print(list1)