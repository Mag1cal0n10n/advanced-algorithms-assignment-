class HashTable:
    def __init__(self, size):
        self.size = size 
        self.table = [None] * size # Initialize the hash table with None values
        self.count = 0

    def _hash(self, key):
        return key % self.size

    def display(self):
        for i in range(self.size):
            print(f"Slot [{i}]: {self.table[i]}")

    def insert(self, key, value):
        if self.count == self.size:
            print("Hash table is full!")
            return -1

        index = self._hash(key)

        while self.table[index] is not None:
            stored_key, stored_value = self.table[index]

            # Handles the case where the key already exists
            if stored_key == key:
                self.table[index] = (key, value) # update existing key
                return index
            index = (index + 1) % self.size # linear probing

        self.table[index] = (key, value)
        self.count += 1
        return index

# --- test ---
ht = HashTable(10)
print("1042 ->", ht.insert(1042, "Paracetamol"))
print("1035 ->", ht.insert(1035, "Ibuprofen"))
print("2052 ->", ht.insert(2052, "Vitamin C"))
print("3062 ->", ht.insert(3062, "Cough Syrup"))
ht.display()