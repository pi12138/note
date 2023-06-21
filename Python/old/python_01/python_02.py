#字符串
#1.转义字符,使用\	
str1 = "Let's go!";
print(str1)	

str2 = 'Let\'s go!';
print(str2)

str3 = "C:\\user";
print(str3)

str4 = "i love \r\n\t learn!"
print(str4)

#字符串格式化
# %d表示此处应该放入一个整数
# %s表示此处应该放入一个字符串
str5 = "i love %s"
print(str5)
print("i love %s"%"learn")
print( str5%"learn")

str6 = "i am %d years old!"
print(str6%19)
	
str7 = "i am %s, i am %d years old"
print(str7%("zhouyoupeng", 20))

#format 函数格式化，推荐使用。
str8 = "i love {}".format("study")
print(str8)

str9 = "My name is {0},i am {1} years old,i am {1} years old,My name is {0}".format("zhouyoupeng",18)
print(str9)

str5 = None
print(str5)

#表达式，运算符
a = 9-2/3
print(a)

b = 9%4 #取余
print(b)

c = 9//4 #取商
print(c)

d = 9**4 #求幂
print(d)
f = 3**3
print(f)

#比较运算符
e = 120
g = e == 3**5
print("g的值为",g)

#逻辑运算符(and,or,not)
x1 = True
x2 = False
x3 = True
x4 = x1 and x2 or x3
print(x4)

#成员运算符 （in ， not in）
y1 = {1,2,3,4,5}
y2 = 6
y3 = y2 in y1
print(y3)
print(y2 not in y1)

#身份运算符(is,is not)
m1 = 10
m2 = 10
print(m1 is m2)

n1 = "i love learn"
n2 = "i love learn"
print(n1 is n2)
