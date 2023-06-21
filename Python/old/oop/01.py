# 类的定义
class Student():

    pass    # 此处pass必有，pass代表直接跳过


zyp = Student()     # 实例化一个对象


class StudentPython( ):
    name = None
    age = 18
    course = 'Python'

    def Do_homework(self):
        print("I do homework!")
        return None

zyp = StudentPython()   #实例化一个对象
print(zyp.name)
print(zyp.age)
print(zyp.course)
zyp.Do_homework()

print(zyp.__dict__)        #对象所有成员检查
print(StudentPython.__dict__)   #类所有成员检查

class Person():
    name = 'zyp'
    age = 20

    def play(self):          #self并不是关键字，但是不可缺少，可以用其他名字代替
        self.name = '周友鹏'
        self.age = 21

print(Person.name)
print(Person.age)
print(id(Person.name))      #与下面实例化后的对象id进行对比
print(id(Person.age))

print("*" * 20)

p1 = Person()               #实例化一个对象

print(p1.name)
print(p1.age)
print(id(p1.name))
print(id(p1.age))
print("*" * 20)



# print(Person.name)
# print(Person.age)
# print(id(Person.name))      #与下面实例化后的对象id进行对比
# print(id(Person.age))

p2 = Person()

print(Person.__dict__)
print(p2.__dict__)

p2.name = '周友鹏'
p2.age = 21

print(Person.__dict__)
print(p2.__dict__)

class Teacher():
    name = 'zyp'
    def say(self):
        self.name = '周友鹏'
        self.age = 20
        print('hello {0}'.format(self.name))
        print('hello {0}'.format(__class__.name))   #可以使用__class__.变量名访问类的成员变量  ****

    def sayAgain():
        print("hello again!")
        # print(name)
        print(__class__.name)       #可以使用__class__.变量名访问类的成员变量  ****

t1 = Teacher()

# print(t1.name)
# print(t1.age)

t1.say()
# t1.sayAgain()             #sayAgain()函数没有self，无法调用           ***
# Teacher.say()
Teacher.sayAgain()          #调用绑定类函数得使用类名           ****


