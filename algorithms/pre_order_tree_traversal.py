"""
PRE-ORDER TREE TRAVERSAL : in this algorithms/traversal style root node is first traversed then
left most node is traversed first and to its parent node then down to right child
and back again to parent's parent node and so on.

THIS IS THE TRAVERSAL PATTERN ->
        1
      /   \
     2     5
    / \    / \
   3   4  6   7
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# creating an instance of Node class and creating tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

"""
IMPLEMENTING TRAVERSAL
"""
def PreOrderTraversal(root):
    if root:
        print(root.value)
        PreOrderTraversal(root.left)
        PreOrderTraversal(root.right)

PreOrderTraversal(root)
