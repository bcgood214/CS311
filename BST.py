from Node import Node
from random import randint
	
# The updated class
class BST:
	
	def __init__(self):
		self.root = None
		
	
	def tree_insert(self, z):
		y = None
		x = self.root
		while x is not None:
			y = x
			if z.data < x.data:
				x = x.left
			else:
				x = x.right
		z.parent = y
		if y is None:
			self.root = z
		elif z.data < y.data:
			y.left = z
		else:
			y.right = z
	
	def search(self, data):
		x = self.root
		while x is not None and data != x.data:
			if data < x.data:
				x = x.left
			else:
				x = x.right
		return x
	
	def insert_left(self, z):
		if self.root is None:
			self.root = z
		else:
			x = self.root
			while x.left is not None:
				x = x.left
			z.parent = x
			x.left = z
	
	def tree_min(self, x):
		while x.left is not None:
			x = x.left
		return x
	
	def tree_max(self, x):
		while x.right is not None:
			x = x.right
		return x
	
	def lvr(self, n):
		if n is not None:
			self.lvr(n.left)
			print(n.data)
			self.lvr(n.right)
	
	def preorder(self, n):
		if n is not None:
			print(n.data)
			self.preorder(n.left)
			self.preorder(n.right)
			
	def transplant(self, u, v):
		if u.parent is None:
			self.root = v
		elif u is u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		if v is not None:
			v.parent = u.parent
	
	def tree_delete(self, z):
		if z.left is None:
			self.transplant(z, z.right)
		elif z.right is None:
			self.transplant(z, z.left)
		else:
			y = self.tree_min(z.right)
			if y.parent is not z:
				self.transplant(y, y.right)
				y.right = z.right
				y.right.parent = y
			self.transplant(z, y)
			y.left = z.left
			y.left.parent = y
			
	def tree_successor(self, x):
		if x.right is not None:
			return self.tree_minimum(x.right)
		y = x.parent
		while y is not None and x == y.right:
			x = y
			y = y.parent
		return y
		
	def check(self, node):
		if node is not None:
			if node.left is not None and node.left.data > node.data:
				return False
			if node.right is not None and node.right.data < node.data:
				return False
			if not self.check(node.left):
				return False
			if not self.check(node.right):
				return False
		return True