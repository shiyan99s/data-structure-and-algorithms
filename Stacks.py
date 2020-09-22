class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, new_val):
        new_val = Node(new_val)
        new_val.next = self.head
        self.head = new_val

    def delete_first(self):
        if self.head:
            deleted = self.head
            temp = deleted.next
            self.head = temp
            return deleted.value
        else:
            return None

    def print_stack(self):
        temp = self.head
        arr = []
        while temp:
            arr.append(temp.value)
            temp = temp.next
        return arr


class Stacks:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, new_val):
        self.ll.insert_first(new_val)

    def pop(self):
        return self.ll.delete_first()

    def print(self):
        return self.ll.print_stack()

if __name__ == '__main__':
    s = Stacks()
    s.push(1)
    s.push(3)
    s.push(5)
    s.push(7)
    s.push(11)
    print(s.print())
    print(s.pop())
