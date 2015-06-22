'''
	this fucntion def lca() tries to find least common ancestor. The algorithm run in O(n) time. 
	There is no additional memory required for this algorithm.

	The algorithm uses a bottom up approuch.
'''

class Node(object):
	
	def __init__(self, key, parent=None):
		self.right= None
		self.left = None
		self.key = key
		self.parent = parent


class Tree():

	def __init__(self):
		self.node = Node(1)
		self.root = self.node
		self.root.parent = self.root
	
	def lca(self, node1, node2):
		if not isinstance(node1, Node) or not isinstance(node2, Node):
			print "In valid Input"
			return  

		if node2 == node1:
			print  "Ancestor is " ,node1.key
			return

		elif node1.parent == node2:
			print  "Ancestor is " ,node2.key
			return
		
		elif node2.parent == node1:
			print  "Ancestor is " ,node1.key
			return
		
		else:
			self.lca(node1.parent, node2.parent)
		
		return 



# some sample test
'''

					1
				  /   \
				2		3
			  /   \    /  \
			 4	   5  6	   7
			 			  /  \
			 			 8    9 
this following code below creats a sample tree describied above
'''		
tree  = Tree()

tree.root.left = Node(2, tree.root)
tree.root.right = Node(3, tree.root)

tree.root.left.left = Node(4, tree.root.left)
tree.root.left.right = Node(5, tree.root.left)

tree.root.right.left = Node(6, tree.root.right)
tree.root.right.right = Node(7, tree.root.right)

tree.root.right.right.right = Node(8, tree.root.right.right)
tree.root.right.right.left = Node(9, tree.root.right.right) 

tree.lca(tree.root.right.right.left, tree.root.right.right.right)




