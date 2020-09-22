class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)

    def preorder_search(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            else:
                return self.preorder_search(current.left, find_val) or self.preorder_search(current.right, find_val)
        return False

    def print(self):
        return self.preorder_print(self.root, "")[:-1]

    def preorder_print(self, current, traversal):
        if current:
            traversal += str(current.value) + "-"
            traversal = self.preorder_print(current.left, traversal)
            traversal = self.preorder_print(current.right, traversal)

        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.search(4))
print(tree.search(6))

print(tree.print())
