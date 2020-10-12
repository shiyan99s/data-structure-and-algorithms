class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert_node(self, new_val):
        return self.insert_node_helper(self.root, new_val)

    def insert_node_helper(self, start, new_val):
        if start:
            if start.value > new_val:
                if start.left:
                    self.insert_node_helper(start.left, new_val)
                else:
                    start.left = Node(new_val)
            else:
                if start.right:
                    self.insert_node_helper(start.right, new_val)
                else:
                    start.right = Node(new_val)
        else:
            self.root = Node(new_val)


    def search_normal(self, find_val):
        return self.search_normal_helper(self.root, find_val)

    def search_normal_helper(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            elif start.value > find_val:
                return self.search_normal_helper(start.left, find_val)
            else:
                return self.search_normal_helper(start.right, find_val)

        else:
            return False

    def search_preorder(self, find_val):
        return self.search_preorder_helper(self.root, find_val)

    def search_preorder_helper(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.search_preorder_helper(start.left, find_val) or self.search_preorder_helper(start.right, find_val)

        return False

    def print_preorder(self):
        return self.print_preorder_helper(self.root, "")[:-1]

    def print_preorder_helper(self, start, traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.print_preorder_helper(start.left, traversal)
            traversal = self.print_preorder_helper(start.right, traversal)
        return traversal


if __name__ == '__main__':
    tree = BinarySearchTree(25)
    tree.insert_node(15)
    tree.insert_node(50)
    tree.insert_node(10)
    tree.insert_node(22)
    tree.insert_node(35)
    tree.insert_node(70)
    tree.insert_node(4)
    tree.insert_node(12)
    tree.insert_node(18)
    tree.insert_node(24)
    tree.insert_node(31)
    tree.insert_node(44)
    tree.insert_node(66)
    tree.insert_node(90)
    print(tree.print_preorder())
