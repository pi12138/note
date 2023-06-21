

from collections import namedtuple

stu = namedtuple('Student', ['id', 'all_result', 'n'])

stu_info = [
('zyp', 300, 3),
('gzy', 250, 3),
('zy', 200, 3),
]
def Grade(stu_info):
    # avg = 0
    for info in stu_info:
        avg = info[1]/info[2]
        print(avg)
Grade(stu_info)
# 下标操作通常会让代码表意不清晰，并且非常依赖记录的结构。下面是使用命名元组的版本：
def Grade_new(stu_info):
    for info in stu_info:
        s1 = stu(*info)
        avg = s1.all_result/s1.n
        print(avg)
Grade_new(stu_info)