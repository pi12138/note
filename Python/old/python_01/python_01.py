if True:
	print("True");
else:
	print("false");

print("frist python exe")

print("learning python")

# 1.行注释，以#开头！
# 2.块注释，以三个单引号开始，以三个单引号结束，中间部分注释，'''这里面是注释'''

#程序 = 数据结构 + 算法

#变量：可以重复使用的一个量，或者叫一个代号。

#查看关键字方法
import keyword #引入关键字模块
print(keyword.kwlist)

#变量声明
#var_name = var_value
var1 = 10;
var2 = 30;

print(var1)
print(var2)

var3 = var4 = var5 = 100;
print(var3,var4,var5)

age1,age2,age3 = 10,20,30;
print(age1,age2,age3)

#Number数字类型
#数字类型没有大小限制
height = 180;
weight = 133.3;
skill = .6;
print(height,weight,skill)

#科学计数法
#写法e/E后面跟整数表示10的指数
#1.734e3 == 1734.0
scientific_notation = 1.734e3;
print(scientific_notation)

#复数
complex_1 = 3+5j;
print(complex_1)

#布尔值，只有两个值True/False，可以和数字进行运算
num = 19 + True;
print(num)

#字符串
#单引号，双引号，三引号
love = "i love learning"
print(love)
love = "我爱学习"
print(love)