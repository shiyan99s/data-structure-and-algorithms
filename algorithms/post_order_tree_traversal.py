"""
POST-ORDER TREE TRAVERSAL : in this algorithms/traversal style left most node is traversed first
and to its siblings node then down to its parent node and so on back till root and same
traveral in right tree

THIS IS THE TRAVERSAL PATTERN ->
        7
      /   \
     3     6
    / \    / \
   1   2  4   5
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# creating an instance of Node class and creating tree
root = Node(7)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(2)
root.right = Node(6)
root.right.left = Node(4)
root.right.right = Node(5)

"""
IMPLENTING TRAVERSAL
"""

def PostOrderTraversal(root):
    if root:
        PostOrderTraversal(root.left)
        PostOrderTraversal(root.right)
        print(root.value)

PostOrderTraversal(root)
