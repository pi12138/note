"""用列表实现双端队列"""


class Deque(object):
    """双端队列"""

    def __init__(self):
        self.__items = []

    def add_front(self, item):
        # 队列头部添加
        self.__items.insert(0, item)

    def add_rear(self, item):
        # 队列尾部添加
        self.__items.append(item)

    def remove_front(self):
        # 头部移除
        return self.__items.pop(0)

    def remove_rear(self):
        # 尾部移除
        return self.__items.pop()

    def is_empty(self):
        return self.__items == []

    def size(self):
        return len(self.__items)


if __name__ == "__main__":
    deque = Deque()
    deque.add_rear('one')
    deque.add_rear('two')
    deque.add_rear('three')
    deque.add_rear('four')

    print(deque.remove_rear())
    print(deque.remove_front())