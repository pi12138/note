# Python中的可哈希对象和不可哈希对象

- Python的所有不可变的内置对象都是可hashable的，但可变容器(如列表或字典)并非如此。对于用户定义的类的实例，默认情况下是可哈希的；它们都是不相等的，并且它们的哈希值都是id()。

## 可哈希对象

- Number
- Str
- Tuple(当tuple对象中包含有不可哈希对象时，tuple对象也是不可哈希的)

## 不可哈希对象

- List
- Dict
- Set

## hash(obj)

- 返回对象的哈希值

## Python中的自定义对象

- 内置的 hash() 方法可以用于所有的内置类型对象。如果是自定义对象调用 hash()的话，实际上运行的是自定义的 `__hash__`。

```python
In [25]: class New:
    ...:     def __hash__(self):
    ...:         return 1111
    ...:
    ...:

In [26]: n = New()

In [27]: hash(n)
Out[27]: 1111
```

## 检测对象是否可散列

- `isinstance(my_obj, Hashable)`。
- Hashable 在 模块 collections 中。


