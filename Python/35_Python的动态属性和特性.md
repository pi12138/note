# Python的动态属性和特性

- 在 Python 中，数据的属性和处理数据的方法统称属性（attribute）。其实，方法只是可调用的属性。
- 除了这二者之外，我们还可以创建特性（property），在不改变类接口的前提下，使用存取方法（即读值方法和设值方法）修改数据属性。
- 可以在自定义的类中借助 `__getattr__`和`__setattr__`来实现动态属性
- 借助 @property 装饰器实现特性

## 特性

- 特性会覆盖实例属性	
- 特性都是类属性，但是特性管理的其实是实例属性的存取。
- 如果实例和所属的类有同名数据属性，那么实例属性会覆盖（或称遮盖）类属性————至少通过那个实例读取属性时是这样。

- obj.attr 的调用过程
	- 先从 `obj.__class__`中寻找是否有名为 attr 的特性
	- 如果没有再从obj中寻找是否有 attr 属性

```Python
In [60]: class Test: 
...:     @property 
...:     def prop(self): 
...:         print("先执行这个函数") 
...:         return "prop" 
...:                                                                                                                

In [61]: t = Test()                                                                                                     

In [62]: vars(t)                                                                                                        
Out[62]: {}

In [63]: vars(Test)                                                                                                     
Out[63]: 
mappingproxy({'__module__': '__main__',
              'prop': <property at 0x7f44b0540650>,
              '__dict__': <attribute '__dict__' of 'Test' objects>,
              '__weakref__': <attribute '__weakref__' of 'Test' objects>,
              '__doc__': None})

In [64]: t.__dict__['prop'] = "object prop"                                                                             

In [65]: vars(t)                                                                                                        
Out[65]: {'prop': 'object prop'}

In [66]: t.prop                                                                                                         
先执行这个函数
Out[66]: 'prop'
```