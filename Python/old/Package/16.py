import time

# 时间模块属性

# timezone :当前时区和UTC时间相差的秒数，在没有夏令时的情况下的间隔
# altzone: 获取当前时区和UTC时间相差的秒数，在有夏令时的情况下
# daylight: 检测当前时区是否是夏令时状态， 0 表示不是夏令时

print(time.timezone)
print(time.daylight)


# time.time() 		# 得到时间戳
print(time.time())


# time.localtime()		# 得到当前时间的时间结构
# 可以通过点号操作符得到相应的属性元素内容
t = time.localtime()
print(t)
print(type(t))


# time.asctime(时间元组)		# 返回元组正常字符串化之后的时间格式
help(time.asctime)
ta = time.asctime(t)
print(ta)
print(type(ta))


# time.ctime()			# 获取字符串化的当前时间
tc = time.ctime()
print(tc)
print(type(tc))


# time.mktime(时间元祖)			# 使用时间元组获取对应的时间戳
t2 = time.localtime()
tm = time.mktime(t2)
print(tm)
print(type(tm))


# time.sleep(n)			# 使程序进入睡眠，n秒后继续
help(time.sleep)
# for i in range(1, 10):
# 	print(i)
# 	time.sleep(1)


## 测试time.sleep()
t3 = time.localtime()
# print(t3)
ts1 = t3.tm_sec

time.sleep(3)
t4 = time.localtime()
ts2 = t4.tm_sec

print(ts2 - ts1)


# time.strftime():将时间元祖转化为自定义的字符串格式
# 2018 9.13 12:13
help(time.strftime)
t5 = time.localtime()
ts1 = time.strftime('%Y %m.%d %H:%m', t5)
print(ts1)