class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        print(self.preorder_search(self.root, find_val))

    def preorder_search(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            else:
                return self.preorder_search(current.left, find_val) or self.preorder_search(current.right, find_val)
        return False

    def print(self):
        print(self.inorder_print(self.root, "")[:-1])

    def inorder_print(self, current, traversal):
        if current:
            traversal = self.inorder_print(current.left, traversal)
            traversal += str(current.value) + "-"
            traversal = self.inorder_print(current.right, traversal)

        return traversal

    def insert(self, value):
        return self.insert_helper(self.root, value)

    def insert_helper(self, current, value):
        if current is None:
            return Node(value)
        else:
            if current.value == value:
                return root
            elif current.value > value:
                current.left = self.insert_helper(current.left, value)
            else:
                current.right = self.insert_helper(current.right, value)

        return current

    def successorNode(self, value):
        current = value
        if current.left is not None:
            current = current.left

        return current

    def delete(self, value):
        return self.delete_helper(self.root, value)

    def delete_helper(self, current, value):
        if current is None:
            return current

        if current.value > value:
            current.left = self.delete_helper(current.left, value)
        elif current.value < value:
            current.right = self.delete_helper(current.right, value)
        else:
            # if Node has one child or no child
            # copy children into temp variable
            # and return it to grandparent
            if current.left is None:
                temp = current.right
                current = None
                return temp
            elif current.right is None:
                temp = current.left
                current = None
                return temp

            # Node has two children nodes
            # Find inorder successor node
            # store it in a temp variable
            temp = self.successorNode(current.left)

            # Change the current value
            # to inorder successor's value
            current.value = temp.value

            # Delete inorder successor
            current.right = self.delete_helper(current.right, temp.value)

        return current

    def kthSmallest(self, value):
        print(self.kthSmallest_helper(self.root, [], value)[value-1])

    def kthSmallest_helper(self, current, traversal, value):
        if current:
            traversal = self.kthSmallest_helper(current.left, traversal, value)
            traversal.append(current.value)
            traversal = self.kthSmallest_helper(
                current.right, traversal, value)

        return traversal


tree = BinaryTree(50)
# Better insertion way
keys = [30, 20, 40, 70, 60, 80]
for key in keys:
    root = tree.insert(key)

tree.print()
tree.kthSmallest(2)
