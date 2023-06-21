import timeit
import time
import random

def quick_sort(alist, start, end):
	'''快速排序实现'''

	# 递归结束条件
	if start >= end:
		return 

	# 选取选取列表第一个元素为基准'pivot'
	pivot = alist[start]

	# 两个游标，low为从左到右的游标，high为从右到左的游标
	low = start
	high = end

	# 当游标low，和high不重合时执行循环
	while low < high:
		# 右边high指向的值应该大于基准值pivot，游标左移
		while alist[high] >= pivot and low < high:
			high -= 1
		# 当游标high指向的值小于基准值pivot时,将high位置的值放到low位置上
		alist[low] = alist[high]

		# 左边low指向位置的值应该小于基准值pivot，游标右移
		while alist[low] < pivot and low < high:
			low += 1
		# 当游标low指向的值大于基准值pivot时，将low位置的值放到high位置上
		alist[high] = alist[low]

	# 退出循环时low=high，将基准值放到该位置
	alist[low] = pivot

	# 递归执行上面的步骤
	# 基准值左边部分
	quick_sort(alist, start, low-1)
	# 基准值右边部分
	quick_sort(alist, low+1, end)

def random_list(n):
	'''随机生成n个1-100之间的随机整数'''
	num_list = []

	for i in range(0, n):
		num = random.randint(1, 100)
		num_list.append(num)

	return num_list


if __name__ == "__main__":
	l1 = random_list(10000 )
	# print(l1)
	time1 = time.time()
	quick_sort(l1, 0, len(l1)-1)
	time2 = time.time()
	# print(l1)
	print("time:", time2-time1)

	# 创建一个Timer对象
	# t1 = timeit.Timer('quick_sort(l1, 0, len(l1)-1)', 'from __main__ import quick_sort, l1')
	# print(t1.timeit(1000000))
	# print(t1.timeit(1))


