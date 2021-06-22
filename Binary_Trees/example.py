from BinaryTree import BinaryTree
from Node import Node

#setting up Binary Tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# printing pre-order traversal
print(tree.printTree(tree,"preorder"))