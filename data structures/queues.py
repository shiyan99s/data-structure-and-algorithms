class Queue(object):
    def __init__(self):
        self.storage = []

    def enqueue(self, new_val):
        self.storage.append(new_val)

    def dequeue(self):
        return self.storage.pop(0)

    def peek(self):
        return self.storage[0]

    def print(self):
        print(self.storage)

q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(5)
q.enqueue(8)
print(q.dequeue())
print(q.peek())
q.print()
