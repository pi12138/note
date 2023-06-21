# Python集合

- 集合中的元素必须是可散列的(hashable)，set 类型本身是不可散列的，但是 frozenset 可以。

## 注意

- 集合本身是可变数据类型，但是里面面的元素必须是不可变数据类型的(不能是列表，字典，集合)

```python
In [4]: set1 = set()

In [5]: set1
Out[5]: set()

In [6]: set1.add([1,2])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-c79e573968af> in <module>()
----> 1 set1.add([1,2])

TypeError: unhashable type: 'list'
```

## frozenset()

- 不可变的集合
- frozenset 可以用作 set 的元素

```python
In [14]: fro1 = frozenset(['1', 1])

In [15]: fro1
Out[15]: frozenset({1, '1'})

In [16]: set1.add(fro1)

In [17]: set1
Out[17]: {frozenset(), frozenset({1, '1'})}
```

## 集合推导式

```python
In [20]: set2 = {i for i in range(0, 10)}

In [21]: set2
Out[21]: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

## 集合的特点

- 集合里的元素必须是可散列的。
- 集合很消耗内存。
- 可以很高效地判断元素是否存在于某个集合。
- 元素的次序取决于被添加到集合里的次序。
- 往集合里添加元素，可能会改变集合里已有元素的次序。

## 集合生成式

```Python
c = {i for i in range(1, 10)}
```

- 注意集合生成式和字典生成式的区别