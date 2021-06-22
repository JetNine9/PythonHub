# video ref: https://www.youtube.com/watch?v=6oL-0TdVy28
from Node import Node

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    #prints a specific traversal type of nodes in a binary tree
    def printTree(self, tree, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        else: 
            print("Traversal type is not supported")
            return False    

    #algorithm for pre-order traversal
    def preorder_print(self, start, traversal):
        """ Starts from root -> left -> right """

        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal 


