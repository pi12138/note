
def binary_search(alist, elem):
	first = 0
	last = len(alist) - 1

	while first <= last:
		mid_point = int((first + last)/2)

		if alist[mid_point] == elem:
			return mid_point
		elif alist[mid_point] > elem:
			last = mid_point - 1
		elif alist[mid_point] < elem:
			first = mid_point + 1

	return False


if __name__ == "__main__":
	a = [1, 2, 3, 4, 5, 6]
	b = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

	res1 = binary_search(a, 6)
	res2 = binary_search(b, 13)
	
	print(res1)
	print(res2)