class Stacks(object):
    def __init__(self):
        self.storage = []

    def push(self, new_val):
        self.storage.append(new_val)

    def pop(self):
        return self.storage.pop()

    def print(self):
        print(self.storage)

s = Stacks()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
s.print()
