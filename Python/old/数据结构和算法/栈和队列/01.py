"""使用列表实现栈"""


class Stack(object):
    """栈"""
    def __init__(self):
        """初始化一个栈"""
        # 私有,禁止类外部访问
        self.__items = []

    def push(self, item):
        """添加一个新元素到栈顶"""
        self.__items.append(item)

    def pop(self):
        """弹出栈顶元素"""
        self.__items.pop()

    def peek(self):
        """返回栈顶元素"""
        # 判断列表是否为空，如果不判断，当列表为空时，返回会报错
        if self.__items:
            return self.__items[len(self.__items) - 1]
            # return self.__items[-1]   # 与上面效果一样
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__items == []
        # return not self.__items       # 与上面效果一样

    def size(self):
        """返回栈的元素个数"""
        return len(self.__items)


if __name__ == '__main__':
    s = Stack()
    s.push('one')
    s.push('two')
    s.push('three')
    print(s.size())
    print(s.peek())
    print("*" * 50)
    s.pop()
    print(s.size())
    print(s.peek())