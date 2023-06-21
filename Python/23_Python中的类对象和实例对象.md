# Python 中的类对象和实例对象

## 概念

- 类对象： 就是类本身
- 实例对象： 由类实例化出来的对象

```Python
In [1]: class Person(object):
   ...:     def __init__(self):
   ...:         pass
   ...:

In [2]: print(Person)
<class '__main__.Person'>

In [3]: p1 = Person()

In [4]: print(p1)
<__main__.Person object at 0x0000022E52AB0D30>
```

- 上面的 Person 就是类对象，而 p1 则是这个类的实例对象

## 类对象的使用

- 类对象支持两种操作：属性引用和实例化。

```Python
In [5]: class Person(object):
   ...:     name = "xxx"
   ...:     age = 20
   ...:
   ...:     def __init__(self):
   ...:         pass
   ...:

In [6]: Person.name
Out[6]: 'xxx'

In [7]: Person.age
Out[7]: 20

In [8]: p1 = Person()

In [9]: print(p1.name, p1.age)
xxx 20

In [10]: p1.name = 'yyy'

In [11]: print(Person.name, p1.name)
xxx yyy
```

- 上面 In[6]和In[7] 是类对象的属性引用，In[8] 为类对象的实例化

- 实例对象唯一操作是属性引用，有两种有效的属性名称，数据属性和方法。

## 类属性、实例属性、类方法、实例方法、静态方法

### 类属性

- 类属性就是类对象所拥有的属性，它被所有类对象的实例对象所共有，在内存中只存在一个副本；
- 对于公有的类属性，在类外可以通过类对象和实例对象访问。

### 实例属性

- 类的实例化对象的属性，属于实例对象独有。

```Python
In [26]: class Person(object):	
    ...:     name = "xxx"	# 类属性
    ...:     age = 20		# 类属性
    ...:
    ...:     def __init__(self):
    ...:        self.addr = "China"		# 实例属性
    ...:
    ...:

In [27]: p1 = Person()

In [28]: Person.name
Out[28]: 'xxx'

In [29]: Person.age
Out[29]: 20

In [30]: p1.name
Out[30]: 'xxx'

In [31]: p1.addr
Out[31]: 'China'

In [32]: Person.addr
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-32-0ed446385bbc> in <module>
----> 1 Person.addr

AttributeError: type object 'Person' has no attribute 'addr'
In [33]: p1.name = "yyy"

In [34]: print(Person.name, p1.name)
Out[34]: 'xxx' 'yyy'
```

- 类对象和实例对象都可以访问类属性
- 类对象无法访问实例属性
- 类属性只有通过类对象进行修改，实例对象无法修改类属性, 通过实例对象给类属性进行赋值，实际上是给实例对象添加了一条新的属性

### 类方法

- 类方法：是类对象所拥有的方法，需要用修饰器"@classmethod"来标识其为类方法，
- 对于类方法，第一个参数必须是类对象，一般以"cls"作为第一个参数(只是一个参数命名习惯，也可以换成其他的，不过不推荐)
- 能够通过实例对象和类对象去访问。

```Python
In [36]: class Person(object):
    ...:     name = "xxx"
    ...:     age = 20
    ...:
    ...:     def __init__(self):
    ...:         self.addr = "China"
    ...:
    ...:     @classmethod
    ...:     def hello(cls):
    ...:         return "hello world"
    ...:

In [37]: Person.hello()
Out[37]: 'hello world'

In [38]: Person().hello()
Out[38]: 'hello world'
```

- 类方法的一个用途就是可以对类属性进行修改, 这样的话，实例对象通过调用类方法也可以对类属性进行修改

```Python
In [39]: class Person(object):
    ...:     name = "xxx"
    ...:     age = 20
    ...:
    ...:     def __init__(self):
    ...:         self.addr = "China"
    ...:
    ...:     @classmethod
    ...:     def set_name(cls, value):
    ...:         cls.name = value
    ...:

In [40]: Person().set_name("yyy")

In [41]: Person.name
Out[41]: 'yyy'
```

### 实例方法

- 实例方法：在类中最常定义的成员方法，它至少有一个参数并且必须以实例对象作为其第一个参数，一般以名为"self"的变量作为第一个参数。
- 在类外实例方法只能通过实例对象去调用，不能通过其他方式去调用(其实类对象可以调用实例方法，只不过需要传一个实例对象作为第一个参数)。

```Python
In [42]: class Person(object):
    ...:     name = "xxx"
    ...:     age = 20
    ...:
    ...:     def __init__(self):
    ...:         self.addr = "China"
    ...:
    ...:     def get_addr(self):
    ...:         return self.addr
    ...:

In [43]: p = Person()

In [44]: p.get_addr()
Out[44]: 'China'

In [45]: Person.get_addr()		
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-45-c70e23dcb313> in <module>
----> 1 Person.get_addr()

TypeError: get_addr() missing 1 required positional argument: 'self'

In [46]: Person.get_addr(p)
Out[46]: 'China'
```

- 如上所示，类对象直接调用实例方法会报错，但是将一个实例实例对象作为第一个参数传入后，则可以成功调用实例方法

### 静态方法

- 需要通过修饰器 @staticmethod 来进⾏修饰，静态⽅法不需要多定义参数
- 跟普通函数没什么区别，与类和实例都没有所谓的绑定关系，不论是通过类还是实例都可以引用该方法。

- 静态方法使用场景
	- 如果在方法中不需要访问任何实例方法和属性，纯粹地通过传入参数并返回数据的功能性方法，那么它就适合用静态方法来定义，它节省了实例化对象的开销成本，往往这种方法放在类外面的模块层作为一个函数存在也是没问题的，而放在类中，仅为这个类服务。

```Python
In [54]: class Person(object):
    ...:     name = "xxx"
    ...:     age = 20
    ...:
    ...:     def __init__(self):
    ...:         self.addr = "China"
    ...:
    ...:     @staticmethod
    ...:     def sleep(sec):
    ...:         """暂停几秒"""
    ...:         time.sleep(sec)
    ...:     def do_somethings(self):
    ...:         print("do ......")
    ...:         self.sleep(5)
    ...:         print("end ....")
    ...:

In [55]: p = Person()

In [56]: Person.sleep(2)

In [57]: p.sleep(2)

In [58]: p.do_somethings()
do ......
end ....
```

### 区别

|.....|类对象是否可以调用|实例对象是否可以调用|
|-----|-----------------|------------------|
|类属性|是|是(可以调用但是无法直接修改)|
|实例属性|否|是|
|类方法|是|是|
|实例方法|否(其实可以调用，但是要传入一个实例对象)|是|
|静态方法|是|是|