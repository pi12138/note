import random

def random_list(n):
	'''随机生成n个1-100之间的随机整数'''
	num_list = []

	for i in range(0, n):
		num = random.randint(1, 100)
		num_list.append(num)

	return num_list

if __name__ =="__main__":
	
	print(random_list(1000))	


