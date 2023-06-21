# coding:utf-8


def shell_sort(list):
    """希尔排序"""
    n = len(list)
    gap = n // 2            # 取整,python3中n/2得到的是一个浮点型

    # gap变化到0之前插入算法执行的次数
    while gap > 0:          # while gap >= 1
        # 希尔排序和普通插入排序的算法区别就是gap步长
        for i in range(gap, n):
            for j in range(i, 0, -1):
                if list[j] < list[j-gap]:
                    list[j], list[j-gap] = list[j-gap], list[j]
                else:
                    break
        gap //= 2           # 缩短gap步长,重新执行循环


if __name__ == "__main__":
    list2 = [55, 66, 77, 33, 22, 44, 88, 66]
    print(list2)
    shell_sort(list2)
    print(list2)