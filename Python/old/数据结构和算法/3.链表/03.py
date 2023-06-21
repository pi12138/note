"""单向循环链表"""
"""单链表实现"""


class SingleNode(object):
    """结点类"""
    def __init__(self, item):
        # 结点数据
        self.item = item
        # 下一个结点地址
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node = None):
        # 表头
        self.head = node
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        current = self.head

        if current is None:
            # print("Linklist is empty!")
            return True
        else:
            # print("Linklist is not empty!")
            return False

    def append(self, item):
        """在链表尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，如果为空，head指向新结点
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            # 如果链表不为空，通过链表头遍历链表到最后，然后添加新结点
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            print("The linked list has no elements!")
        else:
            current = self.head
            while current.next != self.head:
                print(current.item, end=', ')
                current = current.next
            # 退出循环时current指向尾结点，但是尾结点未打印，所以打印尾结点
            print(current.item)

    def length(self):
        """链表长度"""
        if self.is_empty():
            print("The link list is 0!")
            return 0
        else:
            # current表示游标用来遍历链表
            # count用来计数
            current = self.head
            count = 1
            while current.next != self.head:
                count += 1
                current = current.next
            # print("The link list is {}".format(count))
            return count

    def add(self, item):
        """链表头部添加元素"""
        node = SingleNode(item)
        # 如果循环链表为空
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            self.head = node

    def insert(self, pos, item):
        """链表指定位置添加元素"""
        # 若位置pos为第一个元素之前则执行头部插入
        # 若位置pos为最后一个元素或者之后则执行尾部插入
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = SingleNode(item)
            current = self.head
            count = 0
            while (pos-1) > count:
                current = current.next
                count += 1
            node.next = current.next
            current.next = node

    def remove(self, item):
        """删除结点"""
        # node = SingleNode(item)
        if self.is_empty():
            print("no node")
        else:
            current = self.head
            previous = None
            # 如果是头结点
            if current.item == item:
                if current.next != self.head:
                    # 多个结点
                    while current.next != self.head:
                        current = current.next
                    current.next = self.head.next
                    self.head = self.head.next
                else:
                    # 只有一个结点
                    self.head = None
            else:
                while current.next != self.head:
                    previous = current
                    current = current.next
                    if current.item == item:
                        # 中间结点
                        previous.next = current.next
                        break
                # 如果是尾结点
                if current.item == item:
                    previous.next = current.next
                else:
                    print("item does not exist")

    def search(self, item):
        if self.is_empty():
            print("This link is empty!")
        else:
            current = self.head
            while current.next != self.head:
                if current.item == item:
                    return True
                current = current.next
            # 退出循环current指向尾结点时
            if current.item == item:
                return True
            return False


if __name__ == "__main__":
    link1 = SingleCycleLinkList()
    print(link1.is_empty())
    link1.append('frist node')
    link1.append('second node')
    link1.append('third node')
    print(link1.is_empty())
    link1.travel()
    print(link1.length())
    link1.add("zero node")
    print(link1.length())
    link1.travel()
    print("*" * 50)
    link1.insert(2, 'two node')
    link1.travel()
    print("*" * 50)
    link1.remove('two node')
    link1.travel()
    print("*" * 50)
    print(link1.search('two node'))
    print(link1.search('zero node'))
    print("*" * 50)
    link1.remove("third node")
    link1.travel()
    link1.remove('zero node')
    link1.travel()
