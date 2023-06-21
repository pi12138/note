def bubble_sort(alist):
	n = len(alist)

	if n <= 1:
		return alist

	for i in range(n-1, 0, -1):
		# i 表示每次循环比较的次数，逐渐减小
		for j in range(0, i):
			if alist[j] > alist[j+1]:
				# 升序
				alist[j], alist[j+1] = alist[j+1], alist[j]

	return alist


def select_sort(alist):
	n = len(alist)

	if n <= 1:
		return alist

	for i in range(0, n-1):
		min_location = i 
		for j in range(i+1, n):
			if alist[min_location] > alist[j]:
				min_location = j
		if min_location != i:
			alist[i], alist[min_location] = alist[min_location], alist[i]

	return alist


def insert_sort(alist):
	n = len(alist)

	if n <= 1:
		return alist

	for i in range(1, n):
		for j in range(i, 0, -1):
			if alist[j] < alist[j-1]:
				alist[j], alist[j-1] = alist[j-1], alist[j]

	return alist


if __name__ == "__main__":
	a = [2, 1, 3, 7, 8, 4, 6, 5, 6, 4, 5, 9]
	print(bubble_sort(a))
	
	a = [2, 1, 3, 7, 8, 4, 6, 5, 6, 4, 5, 9]
	print(select_sort(a))

	a = [2, 1, 3, 7, 8, 4, 6, 5, 6, 4, 5, 9]
	print(insert_sort(a))