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
        return counter

    def print(self):
        arr = []
        temp = self.head
        while temp:
            arr.append(temp.value)
            temp = temp.next
        return arr

    def push_front(self, new_val):
        new_val = Node(new_val)
        temp = self.head
        self.head = new_val
        self.head.next = temp

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


if __name__ == "__main__":
    list = LinkedList()
    list.head = Node(3)
    second = Node(5)
    third = Node(8)

    list.head.next = second
    second.next = third

    list.append(11)
    list.push_front(0)
    print(list.get_position(1))
    list.insert(7, 4)
    print(list.print())
    list.delete(5)
    print(list.print())
