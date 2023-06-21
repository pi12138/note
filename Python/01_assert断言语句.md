# assert断言语句

[参考](https://www.cnblogs.com/liuchunxiao83/p/5298016.html)

## python assert断言的作用

python assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。可以理解assert断言语句为raise-if-not，用来测试表示式，其返回值为假，就会触发[异常](http://www.iplaypython.com/jichu/exception.html)。

## assert使用

assert expression [,arguments]

```python
# 当 表达式 的值为真时，不会出现任何问题
In [5]: assert 1==1

# 当 表达式 的值为假时会抛出异常
In [6]: assert 1==0
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-6-788ee363e0a2> in <module>()
----> 1 assert 1==0

AssertionError:

# 可以设置参数，当表达式为假时，会抛出后面的参数
In [13]: assert 1==0,"1 != 0"                                                  
---------------------------------------------------------------------------    
AssertionError                            Traceback (most recent call last)    
<ipython-input-13-486513a5587b> in <module>()                                  
----> 1 assert 1==0,"1 != 0"                                                   
                                                                               
AssertionError: 1 != 0                                                         
```

类似于

```python
In [15]: if 1==0:                                                          
    ...:     pass                                                          
    ...: else:                                                             
    ...:     raise AssertionError('1!=0')                                  
    ...:                                                                   
    ...:                                                                   
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-15-4adfd8de4396> in <module>()                              
      2     pass                                                           
      3 else:                                                              
----> 4     raise AssertionError('1!=0')                                   
                                                                           
AssertionError: 1!=0                                                       
```

