"""使用列表实现队列"""


class Queue():
    """队列"""
    def __init__(self):
        """初始化一个空队列"""
        self.__items = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self.__items.append(item)

    def dequeue(self):
        """删除队列头部一个元素，并且返回该元素"""
        return self.__items.pop(0)

    def is_empty(self):
        """判断队列是否为空"""
        return self.__items == []

    def size(self):
        """返回队列长度"""
        return len(self.__items)


if __name__ == "__main__":
    que = Queue()
    print(que.is_empty())
    que.enqueue('one')
    que.enqueue('two')
    que.enqueue('three')
    print(que.size())
    print("*" * 50)
    print(que.dequeue())
    print(que.size())