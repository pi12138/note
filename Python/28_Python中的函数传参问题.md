# Python中的函数传参问题

- Python 唯一支持的参数传递模式是共享传参。
- 共享传参指函数的各个形式参数获得实参中各个引用的副本。也就是说，函数内部的形参是实参的别名。
- 这种方案的结果是，函数可能会修改作为参数传入的可变对象，但是无法修改那些对象的标识（即不能把一个对象替换成另一个对象）。

## 函数可能会修改传入的可变对象

```python
a = [1, 2, 3, 4]                                                                                              

In [124]: def func(val): 
     ...:     val.append(5) 
     ...:                                                                                                               

In [125]: func(a)                                                                                                       

In [126]: a                                                                                                             
Out[126]: [1, 2, 3, 4, 5]
```

- 上例中的a在函数func执行后被修改

- 函数并不会改变不可变对象

```Python
In [129]: def func(v1, v2): 
     ...:     v1 += v2 
     ...:     return v1 
     ...:                                                                                                               

In [130]: a = (1, 2, 3, 4)                                                                                              

In [131]: b = (5, 6)                                                                                                    

In [132]: func(a, b)                                                                                                    
Out[132]: (1, 2, 3, 4, 5, 6)

In [133]: a                                                                                                             
Out[133]: (1, 2, 3, 4)

In [134]: b                                                                                                             
Out[134]: (5, 6)
```

## 不要将使用可变数据类型作为函数的默认参数

```Python
In [136]: class Person: 
     ...:     def __init__(self, pers=[]): 
     ...:         self.pers = pers 
     ...:     def add(self, name): 
     ...:         self.pers.append(name) 
     ...:     def remove(self, name): 
     ...:         self.pers.remove(name) 
     ...:                                                                                                               

In [137]: p1 = Person()                                                                                                 

In [138]: p2 = Person()                                                                                                 

In [139]: p1.add("aaa")                                                                                                 

In [140]: p1.add("bbb")                                                                                                 

In [141]: p1.pers                                                                                                       
Out[141]: ['aaa', 'bbb']

In [142]: p2.add("ccc")                                                                                                 

In [143]: p2.pers                                                                                                       
Out[143]: ['aaa', 'bbb', 'ccc']

In [144]: p1.pers                                                                                                       
Out[144]: ['aaa', 'bbb', 'ccc']

In [145]: p1.pers is p2.pers                                                                                            
Out[145]: True
```

- 上例中，因为将空列表作为默认参数，导致对象p1，p2的属性pers同步，公用一个列表。
- 所以，通常最好使用 None 作为接收可变值的参数的默认值。

## 解决这种问题

```Python
In [154]: class Person: 
     ...:     def __init__(self, pers=None): 
     ...:         if pers is None: 
     ...:             self.pers = [] 
     ...:         else: 
     ...:             self.pers = list(pers) 
     ...:     def add(self, name): 
     ...:         self.pers.append(name) 
     ...:     def remove(self, name): 
     ...:         self.pers.remove(name) 
     ...:                                                                                                               

In [155]: per_list = ["aaa", "bbb", "ccc"]                                                                              

In [156]: p1 = Person(per_list)                                                                                         

In [157]: p2 = Person(per_list)                                                                                         

In [158]: p1.pers is p2.pers                                                                                            
Out[158]: False

In [159]: p1.pers == p2.pers                                                                                            
Out[159]: True
```

- 当我们函数的传入的参数为可变对象时，可以在函数内部对传入的参数进行一个拷贝，避免其和实参相互影响。

```Python
In [160]: def func(a, b): 
     ...:     a = list(a) 
     ...:     b = list(b) 
     ...:     a += b 
     ...:     return a 
     ...:                                                                                                               

In [161]: a = [1, 2, 3]                                                                                                 

In [162]: b = [4, 5]                                                                                                    

In [163]: func(a,b)                                                                                                     
Out[163]: [1, 2, 3, 4, 5]

In [164]: a                                                                                                             
Out[164]: [1, 2, 3]

In [165]: b                                                                                                             
Out[165]: [4, 5]

```

- 除非这个方法确实想修改通过参数传入的对象，否则在类中直接把参数赋值给实例变量之前一定要三思，因为这样会为参数对象创建别名。如果不确定，那就创建副本。