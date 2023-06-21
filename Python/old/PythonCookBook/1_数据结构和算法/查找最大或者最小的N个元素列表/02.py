'''
两个函数都能接受一个关键字参数，用于更复杂的数据结构中
'''
import heapq


portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# lambda x:y 表示输入参数x，返回值为y
# 类似
# def fun(x):
#   return y
cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
# 译者注：上面代码在对每个元素进行对比的时候，会以 price 的值进行比较。
print('cheap:',cheap)
print('expensive:',expensive)