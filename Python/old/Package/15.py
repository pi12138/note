# 

import calendar

# calendar.calendar(theyear, w=2, l=1, c=6, m=3)函数
# 返回一个多行字符串格式的year年年历，m代表m个月一行，两个月份之间显示间隔距离为c。 
# 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
# help(calendar.calendar)			# 查看函数帮助

# cal = calendar.calendar(2018)
# print(cal)


# calendar.isleap(year) 	# 判断该年是否为闰年
help(calendar.isleap)
print(calendar.isleap(2020))


# calendar.leapdays(year1, year2)	 	# 返回[year1, year2)之间的闰年数且year1 <= year2
help(calendar.leapdays)
print(calendar.leapdays(2000, 2018))


# calendar.month(theyear, themonth, w=0, l=0)			# 获取某个月日历
help(calendar.month)
print(calendar.month(2018, 9))


# calendar.monthrange(year, month)		# 以元组形式返回该月是周几开始的以及这个月有多少天
help(calendar.monthrange)
# print(calendar.monthrange(2018, 9))	# 返回一个元组
for x in calendar.monthrange(2018, 9):
	print(x)


# calendar.monthcalendar(year, month)	# 返回一个月每天的矩阵列表，矩阵中没有的天数用0代替
help(calendar.monthcalendar)
print(calendar.monthcalendar(2018, 9))
print(type(calendar.monthcalendar(2018, 9)))


# calendar.prcal(theyear, w=0, l=0, c=6, m=3) 			# 直接打印日历
help(calendar.prcal)
# calendar.prcal(2018)


# calendar.prmonth(year, month)			# 直接打印月日历


# calendar.weekday(year, month, day)	# 获取周几
print(calendar.weekday(2018, 9, 13))

