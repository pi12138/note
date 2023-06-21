#三大结构
#1.分支
#2.顺序
#3.循环
a = 10
b = 20
c = 30

if a>10 and b<20 or c>30:
	print(a,b,c)
print("条件不符合！")

if a>10 and b<20 or c>40:
	print("a=",a)
	print("b=",b)
	print("c=",c)
else:
	print("条件不符合！")
	print("存在问题！")

# gender = input("请输入性别:")#input 输出（）里的字符串，接收输入内容返回到程序，返回内容一定是字符串
# if gender == "man":
# 	print("你好，先生")
# else:
# 	print("你好，小姐")

# gender = input("请输入性别：")
# if gender == "man":
# 	print("你好，先生")
# elif gender == "woman":
# 	print("你好，小姐")
# else:
# 	print("你是什么鬼哟！")

# score = input("请输入学生成绩：")
# score = int(score)
# if score>90:
# 	print("A")
# elif score>=80:
# 	print("B")
# elif score>=70:
# 	print("C")
# elif score>=60:
# 	print("D")
# else:
# 	print("不说了，丢人")

#for循环
# name = ["杨浩然","陈世创","靳佳欣","谷嘉欣","王畅","王一凡","汪雨乐"]
# for n in name:
# 	print(n)

# for i in range(1,10): #遍历数字序列，从1到9
# 	print(i)

#for-else语句
name = ["杨浩然","陈世创","靳佳欣","谷嘉欣","王畅","王一凡","汪雨乐"]
for n in name:

	print(n)
else:
	print("这些都是我们班的！")
	print("我们班一共{0}人".format(len(name)))

for i in range(1,11):
	if i%2 == 0:
		print(i)

#while循环
i = 1
sum = 0
while i <= 100:
	sum = sum + i 
	i = i + 1
print("1到100的总和为:",sum)

#银行存款利息问题，本金20000，利息2.7%，存3年
capital = 20000 #本金
interest = 0	#利息
year = 1		#年数
ratepaying = 0	#纳税
income = 0		#收入
print("第1年本金为:{0}".format(capital))
while year <= 3:
	interest = capital * 0.027
	year = year + 1
	capital = capital + interest
	print("第{0}年后本金:{1},第{2}年利息:{3}".format(year,capital,year-1,interest))
ratepaying = (capital - 20000) * 0.2
income = (capital - 20000) * 0.8
print("{0}年后,可以取出{1}人民币,需要纳税{2},共赚了{3}".format(year-1,capital-ratepaying,ratepaying,income))