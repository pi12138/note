import collections

Point = collections.namedtuple('Point', ['x', 'y'])

print(type(Point))
print(Point)
print(Point.__doc__)
# help(collections.namedtuple)

# 实例化
p = Point(11, 22)
print(p)
print("p.x={0}, p.y={1}".format(p.x, p.y))
print("p[0]={0}, p[1]={1}".format(p[0], p[1]))
print(20*"*")

Cricle = collections.namedtuple('Cricle', ['x', 'y', 'r'])

c = Cricle(100, 100, 50)
print(c)
print(type(c))

# 想检验namedtuple是谁的子类
TorF = isinstance(c, tuple)
print(TorF)