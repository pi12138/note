# coding:utf-8


def insert_sort(list):
    """插入排序"""
    n = len(list)

    for i in range(1, n):
        # 后面未排序部分，和前面已排序部分，从右到左比对
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
            else:
                break


def insert_sort2(list):
    """插入排序2"""
    n = len(list)
    for i in range(1, n):
        # 后面未排序部分，和前面已排序部分，从右到左比对
        while i > 0:
            if list[i] < list[i-1]:
                list[i], list[i-1] = list[i-1], list[i]
                i -= 1
            else:
                break


if __name__ == "__main__":
    list1 = [55, 66, 77, 33, 22, 44, 88]
    print(list1)
    insert_sort(list1)
    print(list1)
    print("-" * 50)

    list2 = [55, 66, 77, 33, 22, 44, 88, 66]
    print(list2)
    insert_sort2(list2)
    print(list2)