'''
问题
在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

解决方案
保留有限历史记录正是 collections.deque 大显身手的时候。比如，下面的代码在多行上面做简单的文本匹配，并返回匹配所在行的最后 N行 

讨论
我们在写查询元素的代码时，通常会使用包含 yield 表达式的生成器函数，也就
是我们上面示例代码中的那样。这样可以将搜索过程代码和使用搜索结果代码解耦。如
果你还不清楚什么是生成器，请参看 4.3 节。
使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并
且这个队列已满的时候，最老的元素会自动被移除掉。
在队列两端插入或删除元素时间复杂度都是 O(1) ，而在列表的开头插入或删除元
素的时间复杂度为 O(N) 。

'''

from collections import deque
# import time

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    # print(type(previous_lines))
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open(r'file.txt') as f:
        # print(f)
        # 文件内容一行一行打印
        # for i in f:
        #     print(i)
        #     time.sleep(2) 
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)