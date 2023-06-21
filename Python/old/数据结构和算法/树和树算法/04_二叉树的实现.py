"""
- 节点：通过使用Node类中定义三个属性，分别为elem本身的值，还有lchild左孩子和rchild右孩子
- 树的创建,创建一个树的类，并给一个root根节点，一开始为空，随后添加节点
"""

class Node(object):
	def __init__(self, elem=1, lchild=None, rchild=None):
		self.elem = elem
		self.lchild = lchild
		self.rchild = rchild


class Tree(object):
	def __init__(self):
		self.root = None
		self.tree_list = []
		self.in_list = []
		self.post_list = []

	def add(self, elem):
		node = Node(elem)			

		if self.root is None:
			self.root = node
		else:
			queue = []
			queue.append(self.root)

			while queue:
				cur = queue.pop(0)

				if cur.lchild is None:
					cur.lchild = node
					return
				elif cur.rchild is None:
					cur.rchild = node
					return
				else:
					queue.append(cur.lchild)
					queue.append(cur.rchild)

	def travel(self):
		"""深度优先遍历"""
		tree_list = []

		if self.root is None:
			return tree_list
		else:
			queue = []
			queue.append(self.root)
			tree_list.append(self.root.elem)

			while queue:
				cur = queue.pop(0)
				if cur.lchild is not None:
					tree_list.append(cur.lchild.elem)
					queue.append(cur.lchild)
				if cur.rchild is not None:
					tree_list.append(cur.rchild.elem)
					queue.append(cur.rchild)
			
			return tree_list

	def pre_travel(self, root):
		"""先序遍历"""

		if root is None:
			return
		else:
			self.tree_list.append(root.elem)
			self.pre_travel(root.lchild)
			self.pre_travel(root.rchild)

		return self.tree_list

	def in_travel(self, root):
		"""中序遍历"""
		if root is None:
			return 
		else:
			self.in_travel(root.lchild)
			self.in_list.append(root.elem)
			self.in_travel(root.rchild)

		return self.in_list

	def post_travel(self, root):
		"""后序遍历"""
		if root is None:
			return
		else:
			self.post_travel(root.lchild)
			self.post_travel(root.rchild)
			self.post_list.append(root.elem)

		return self.post_list

if __name__ == "__main__":

	t1 = Tree()
	t1.add("A")
	t1.add("B")
	t1.add("C")
	t1.add("D")
	t1.add("E")
	t1.add("F")
	print(t1.travel())

	print("先序遍历:")
	res = t1.pre_travel(t1.root)
	print(res)

	print("中序遍历:")
	res = t1.in_travel(t1.root)
	print(res)

	print("后序遍历:")
	res = t1.post_travel(t1.root)
	print(res)