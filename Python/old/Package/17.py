import datetime
import time
import timeit
# datetime 常见属性
# datetime.date(year, month, day): 一个理想和的日期，提供year, month, day属性
# help(datetime.date)

# print(datetime.date(2018, 9, 13))
dt = datetime.date(2018, 9, 13)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)


# datetime.datetime			# 提供日期和时间的组合
# 常用类方法
# - today()
# - now()
# - utcnow()
# - fromtimestamp(): 从时间戳返回本地时间

dt2 = datetime.datetime(2018, 9, 13)
print(dt2.today())
print(dt2.now())
print(dt2.utcnow())
# time.time()是为了得到时间戳
print(dt2.fromtimestamp(time.time()))


# datetime.timedelta():表示一个时间间隔
# help(datetime.timedelta)
t3 = datetime.datetime.now()
print(t3.strftime('%Y - %m - %d  %H : %M : %S'))

t4 = datetime.timedelta(hours = 2)	#表示一个时间段，2个小时
# (t3 + t4)表示t3时间往后推延了t4个小时
print((t3 + t4).strftime('%Y - %m - %d  %H : %M : %S'))


# timeit :时间测量工具，可以执行一个代码段或者函数来测量执行时间
#
# list2 = [x for x in range(1, 1000)]		# 列表生成式
# 用timeit对比列表生成式生成列表，和for循环生成列表的耗时
# c = '''									
# list1 = []
# for i in range(1, 1000):
# 	list1.append(i)
# 	'''

# # help(timeit.timeit)
# t5 = timeit.timeit(stmt = c, number = 10000)
# t6 = timeit.timeit(stmt = "[x for x in range(1, 1000)]", number = 10000)
# print(t5)
# print(t6)

# 执行一个函数，测量一个函数的执行时间
# def sum():
# 	for i in range(0,3):
# 		print(i)

# t7 = timeit.timeit(stmt = sum, number = 5)		# 将函数sum执行5遍
# print(t7)


str1 = '''
def Doit(num):
	for i in range(0, num):
		print(i)
'''
# 执行Doit(num)
# setup 负责把环境变量准备好
# 实际上相当于给timeit创造了一个小环境
t8 = timeit.timeit("Doit(num)", setup = str1 + "num = 3", number = 3)
print(t8)