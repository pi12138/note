'''
如果你有一个切片对象 a，你可以分别调用它的 a.start , a.stop , a.step 属性
来获取更多的信息。比如：

另外，你还能通过调用切片的 indices(size) 方法将它映射到一个确定大小的序
列上，这个方法返回一个三元组 (start, stop, step) ，所有值都会被合适的缩小以
满足边界限制，从而使用的时候避免出现 IndexError 异常。比如：
'''

a = slice(5, 50, 2)
print("a.start:{0}, a.stop:{1}, a.step:{2}".format(a.start, a.stop, a.step))

s = 'HelloWorld' 
t_indices = a.indices(len(s))
print(t_indices)

print(range(*a.indices(len(s))))
print(range(*t_indices))

for i in range(*t_indices):
    print(s[i])
