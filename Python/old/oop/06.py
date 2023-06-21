## 3. 多态
####	- 多态就是同一个对象在不同情况下有不同的状态出现
####	- 多态不是语法，是一种设计思想
####	- 多态性：一种调用方式， 不同的执行效果
####	- 多态：同一事物的多种形态，动物分为人类，狗类....

## MiXin设计模式
####	- 主要采用多继承的方式对类的功能进行扩展
#
## 使用Mixin类实现多重继承要非常小心
#### 	-首先它必须表示某一种功能，而不是某个物品，如同Java中的Runnable，Callable等
####	-其次它必须责任单一，如果有多个功能，那就写多个Mixin类
####	-然后，它不依赖于子类的实现
####	-最后，子类即便没有继承这个Mixin类，也照样可以工作，就是缺少了某个功能。
#
class Vehicle(object):
    pass
 
class PlaneMixin(object):
    def fly(self):
        print 'I am flying'
 
class Airplane(Vehicle, PlaneMixin):
    pass

# 可以看到，上面的Airplane类实现了多继承，不过它继承的第二个类我们起名为PlaneMixin，
# 而不是Plane，这个并不影响功能，但是会告诉后来读代码的人，这个类是一个Mixin类。所以从含义上理解，
# Airplane只是一个Vehicle，不是一个Plane。这个Mixin，表示混入(mix-in)，它告诉别人，
# 这个类是作为功能添加到子类中,而不是作为父类，它的作用同Java中的接口。