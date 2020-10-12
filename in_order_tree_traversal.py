"""
IN-ORDER TREE TRAVERSAL : in this algorithms/traversal style left most node is traversed first
and to its parent node then down to right child and back again to parent's parent node and so on.

THIS IS THE TRAVERSAL PATTERN ->
        4
      /   \
     2     6
    / \   /  \
   1   3  5   7
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# creating a instance of class Node to construct tree
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

"""
IMPLENTING TRAVERSAL
"""

def InOrderTraversal(root):
    if root:
        InOrderTraversal(root.left)
        print(root.value)
        InOrderTraversal(root.right)

InOrderTraversal(root)
