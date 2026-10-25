class HashTable:
    def __init__(self, size):
        self.size = size 
        self.table = [None] * size # Initialize the hash table with None values
        self.count = 0

    def _hash(self, key):
        return key % self.size

    def display(self):
        for i in range(self.size):
            if self.table[i] is None:
                print(f"Slot {i}: Empty")
            else:
                key, value = self.table[i] # unpack the (key, value) tuple
                print(f"Slot {i}: {key} -> {value}")

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

    def search(self, key):
        index = self._hash(key)
        checked = 0

        while self.table[index] is not None and checked < self.size:
            stored_key, stored_value = self.table[index]

            if stored_key == key:
                return stored_value
            index = (index + 1) % self.size
            checked += 1

        return None

if __name__ == "__main__":        
    ht = HashTable(10)
    print("1042 ->", ht.insert(1042, "Paracetamol"))
    print("1035 ->", ht.insert(1035, "Ibuprofen"))
    print("2052 ->", ht.insert(2052, "Vitamin C"))
    print("3062 ->", ht.insert(3062, "Cough Syrup"))
    ht.display()

    print("Search 3062:", ht.search(3062))
    print("Search 1035:", ht.search(1035))
    print("Search 9999:", ht.search(9999))
    print("Search 4072:", ht.search(4072))
    print("Search 1036:", ht.search(1036))

    print("\n---Full Table Test---")
    small = HashTable(3)
    print(small.insert(10, "A"))
    print(small.insert(20, "B"))
    print(small.insert(30, "C"))
    print(small.insert(40, "D"))  # Should indicate that the table is full
    print(small.search(30))
    print(small.search(99)) # Should return None
    small.display()