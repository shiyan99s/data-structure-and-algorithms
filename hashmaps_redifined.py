class HashTable:
    def __init__(self):
        self.table = [None] * 1000

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] is not None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def calculate_hash_value(self, string):
        return (ord(string[0]) * 100 + ord(string[1]))

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] is not None:
                if string in self.table(hv):
                    return hv
        return -1

    def print(self):
        for item in self.map:
            print(i)


hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
