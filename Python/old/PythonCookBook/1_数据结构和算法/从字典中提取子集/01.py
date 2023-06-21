'''
问题
你想构造一个字典，它是另外一个字典的子集。

解决方案
最简单的方式是使用字典推导。比如：
'''

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}

new_prices1 = {key:value for key,value in prices.items() if value > 200}
new_prices2 = {key:value for key,value in prices.items() if key in tech_names}

print("new_prices1:", new_prices1)
print("new_prices2:", new_prices2)
'''
讨论
大多数情况下字典推导能做到的，通过创建一个元组序列然后把它传给 dict() 函
数也能实现。比如：
'''

t1 = tuple((key, value) for key, value in prices.items() if value > 200)
# print(t1)
new_prices3 = dict(t1)
print("new_prices3:", new_prices3)

'''
但是，字典推导方式表意更清晰，并且实际上也会运行的更快些（在这个例子中，
实际测试几乎比 dcit() 函数方式快整整一倍）。
有时候完成同一件事会有多种方式。比如，第二个例子程序也可以像这样重写：
'''
new_prices4 = {key:prices[key] for key in prices.keys() & tech_names}
print('new_prices4:', new_prices4)

'''
但是，运行时间测试结果显示这种方案大概比第一种方案慢 1.6 倍。如果对程序运
行性能要求比较高的话，需要花点时间去做计时测试。
'''