'''
问题
如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。那么
怎样才能从这个可迭代对象中解压出 N 个元素出来？

解决方案Python 的星号表达式可以用来解决这个问题。比如，你在学习一门课程，在学期末的时候，你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。如果只有四个分数，你可能就直接去简单的手动赋值，但如果有 24 个呢？这时候星号表达式*就派上用场

'''
# import math
def test(grades):
    first,*middle,end = grades
    print('first:',first)
    print('middle:',middle)
    print('end:',end)

    avg_grade = sum(middle)/len(middle)
    print('avg_grade:',avg_grade)

grades = (100,95,90,85,80,75,70)
test(grades)

