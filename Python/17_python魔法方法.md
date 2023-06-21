# Python魔法方法

## `__getattr__(self, item)`

- 该方法在一个实例调用自己内部不存在的一个属性或者方法时，会自动调用该方法来处理

## `__setattr(self, item, value)`

- 如果要给 item 赋值，就调用这个方法

## `__getattribute__(self, item)`

- 当 name 被访问时自动被调用（注意：这个仅能用于新式类），无论 name 是否存在，都要被调用。

## `__delattr__(self, item)`

- 如果要删除 name，这个方法就被调用。

## `__call__`

- 让类的实例，可以像函数一样被调用(obj())

## `__mro__`

- 获取类的继承关系，返回一个元祖

## `__iter__`

- 如果实现了`__iter__`方法，那么就认为对象是可迭代的。