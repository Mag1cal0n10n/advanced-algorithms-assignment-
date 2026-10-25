class HashTable:
    DELETED = "DELETED" # Tombstone marker for deleted slots
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
            elif self.table[i] is self.DELETED:
                print(f"Slot {i}: Deleted")
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
            if self.table[index] is self.DELETED:
                        index = (index + 1) % self.size
                        checked += 1
                        continue

            stored_key, stored_value = self.table[index]

            if stored_key == key:
                return stored_value
            index = (index + 1) % self.size
            checked += 1

        return None

    def delete(self, key):
        index = self._hash(key)
        checked = 0

        while self.table[index] is not None and checked < self.size:
            if self.table[index] is self.DELETED:
                index = (index + 1) % self.size
                checked += 1
                continue

            stored_key, stored_value = self.table[index]

            if stored_key == key:
                self.table[index] = self.DELETED
                self.count -= 1
                return True
            index = (index + 1) % self.size
            checked += 1

        return False

if __name__ == "__main__":        
    print("\n--- Delete Test ---")
    t = HashTable(17)
    t.insert(1042, "A")
    t.insert(1059, "B")
    t.insert(1076, "C")
    print("Delete 1059:", t.delete(1059))   # expect True
    print("Search 1076:", t.search(1076))   # expect C, i.e. it skips the tombstone!
    print("Delete 9999:", t.delete(9999))   # expect False
    t.display()                             # slot 6 should show Deleted
