class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_val):
        new_val = Node(new_val)
        temp = self.head
        if self.head:
            while temp.next:
                temp = temp.next
            temp.next = new_val
        else:
            self.head = new_val

    def get_position(self, position):
        if position > self.length():
            return ("ERROR: Index out of range.")
        counter = 1
        temp = self.head
        while temp:
            if position == 0:
                return self.head.value
            elif position == counter:
                return temp.next.value
            counter += 1
            temp = temp.next

    def length(self):
        counter = 0
        temp = self.head
        while temp:
            counter += 1
            temp = temp.next

        print(counter)

    def print(self):
        current = self.head
        arr = []
        s = "->"
        while current:
            arr.append(str(current.value))
            current = current.next

        print(s.join(arr))

    # Push new node in front
    def push(self, value):
        value = Node(value)
        value.next = self.head
        self.head = value

    def insert(self, new_val, position):
        new_val = Node(new_val)
        counter = 1
        temp = self.head
        while temp:
            if counter == position-1:
                new_val.next = temp.next
                temp.next = new_val
            temp = temp.next
            counter += 1

    def delete(self, val):
        temp = self.head
        if temp:
            if temp.value == val:
                self.head = temp.next
                temp = None
                return
        while temp:
            if temp.value == val:
                break
            previous = temp
            temp = temp.next
        if temp is None:
            return None

        previous.next = temp.next
        temp = None

    # Reverses the linked list
    # Pointing the current.next to the previous node
    def reverse(self):
        current = self.head
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def rotate(self, k):
        current = self.head
        counter = 1
        # Traverse till kth Node
        while current and counter < k:
            current = current.next
            counter += 1

        # Store the kth Node in a variable
        kthNode = current

        while current.next:
            current = current.next

        # Change the last node to
        # previous head
        current.next = self.head

        # Change head to (k+1)th node
        self.head = kthNode.next

        # kthNode pointing NULL as next
        kthNode.next = None


if __name__ == "__main__":
    ll = LinkedList()
    keys = [10, 20, 30, 40, 50, 60]
    for key in keys:
        root = ll.append(key)

    ll.push(0)
    ll.delete(0)
    ll.reverse()
    ll.reverse()
    ll.print()
    ll.rotate(2)
    ll.print()
