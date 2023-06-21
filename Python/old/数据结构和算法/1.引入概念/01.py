# 如果a+b+c=1000, 且a^2+b^2=c^2(a,b,c为自然数)，如何求出所以a，b，c可能的组合？

import time


# t1 = time.ctime()     # 不能使用ctime，因为ctime返回的是字符串
t1 = time.time()        # time返回的是float类型数据
# for a in range(0, 1001):
#     for b in range(0, 1001-a):
#         for c in range(0, 1001-a-b):
#             if a+b+c == 1000 and a**2 + b**2 == c**2:
#                 print('a:{0},b:{1},c:{2}'.format(a, b, c))
# 上面一段代码执行太慢
for a in range(0, 1001):
    for b in range(0, 1001-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print('a:{0},b:{1},c:{2}'.format(a, b, c))

t2 = time.time()
print("运行时间：", t2-t1)
