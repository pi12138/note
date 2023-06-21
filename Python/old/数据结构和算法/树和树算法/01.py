# coding:utf-8
"""
二叉树的实现
广度优先遍历
"""


class Node(object):
    """树的节点"""
    def __init__(self, item):
        self.item = item
        # 左右子节点
        self.lchild = None
        self.rchild = None


class BinaryTree(object):
    """二叉树"""
    def __init__ (self):
        """二叉树初始化"""
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return 
        else:
            # 借助队列遍历
            queue = []
            queue.append(self.root)
            # 对已有节点遍历
            while queue:
                current = queue.pop(0)
                if current.lchild is None:
                    # 如果左边子节点为空则添加到左边
                    current.lchild = node
                    return
                elif current.rchild is None:
                    current.rchild = node
                    return
                else:
                    # 如果左右子节点均存在，则将左右子节点添加到队列然后继续遍历
                    queue.append(current.lchild)
                    queue.append(current.rchild)

    def travel(self):
        """借助队列进行广度优先遍历（层次遍历）"""
        if self.root is None:
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                current = queue.pop(0)
                print(current.item)
                if current.lchild is not None:
                    queue.append(current.lchild)
                if current.rchild is not None:
                    queue.append(current.rchild)


if __name__ == "__main__":
    bt1 = BinaryTree()

    bt1.add("one")
    bt1.add("Two")
    bt1.add("Three")
    bt1.add("Four")

    bt1.travel()
