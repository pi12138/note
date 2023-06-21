"""双向链表实现"""


class Node(object):
    """双向链表结点"""
    def __init__(self, item):
        self.item = item
        self.next = None
        self.previous = None


class DoubleLinkList(object):
    """双向链表"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        if self.is_empty():
            return 0
        else:
            current = self.head
            count = 0
            while current is not None:
                count +=1
                current = current.next
            return count

    def travel(self):
        if self.is_empty():
            print("The doubly linked list has no nodes!")
        else:
            current = self.head
            while current is not None:
                print(current.item, end=", ")
                current = current.next
            print("")

    def add(self, item):
        """头部插入"""
        node = Node(item)
        node.next = self.head
        self.head.previous = node
        # node.next.previous = node     # 跟上面一句效果类似
        self.head = node

    def append(self, item):
        """尾部插入"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            node.previous = current
            current.next = node

    def insert(self, pos, item):
        """指定位置插入"""
        if pos < 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            current = self.head
            # previous = None
            count = 0
            # 移动到指定位置的前一个位置
            while (pos-1) > count:
                # previous = current
                current = current.next
                count += 1
            node.next = current.next
            node.previous = current
            current.next.previous = node
            current.next = node

    def remove(self, item):
        """删除结点"""
        if self.is_empty():
            return 0
        else:
            current = self.head
            # while current is not None:
            if current.item == item:
                # 如果首结点的元素即是要删除的元素
                if current.next is None:
                    # 如果链表只有这一个节点
                    self.head = None
                else:
                    current.next.previous = None
                    self.head = current.next
                # return
        while current is not None:
            if current.item == item:
                if current.next is None:
                    current.previous.next = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                break
            else:
                current = current.next

    def search(self, item):
        """查找结点"""
        current = self.head
        while current is not None:
            if current.item == item:
                return True
            else:
                current = current.next
        return False


if __name__ == "__main__":
    dll1 = DoubleLinkList()
    dll1.append('one')
    dll1.append('two')
    dll1.append('three')
    dll1.travel()
    dll1.add('zero')
    dll1.travel()
    dll1.insert(2, '2')
    dll1.travel()
    dll1.remove('three')
    dll1.travel()
    print(dll1.search('zero'))