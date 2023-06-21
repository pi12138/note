'''
下面是更多的例子
'''

# 确定目录中是否存在任何.py文件
import os 

files = os.listdir('f:/python/oop/')
print(len(files))

# print(any(name.endswith('.py') for name in files))
if any(name.endswith('.py') for name in files):
    print("There be python")
else:
    print("There no python")


# 将元组输出为CSV
s = ('ACME', 50, 123.45)
print(",".join(str(x) for x in s))


portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

