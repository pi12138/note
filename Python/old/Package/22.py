import random

# random.random() 获取0~1之间的随机小数
# 返回一个0~1之间的随机小数
num1 = random.random()
print('num1 =', num1)


# random.choice(序列)
# 随机返回序列中的某个值
list1 = [i for i in range(0,10)]
print('list1 = ', list1)
num2 = random.choice(list1)
print('num2 =', num2)


# random.shuffle(列表)
# 随机打乱列表
# 返回值为None
random.shuffle(list1)
print('shuffle_list1 = ', list1)


# random.randint(a, b)
# 随机返回一个[a, b]之间的整数
# help(random.randint)
num3 = random.randint(0, 100)
print('num3 = ', num3)