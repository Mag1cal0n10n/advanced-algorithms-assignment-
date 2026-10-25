import random
from hash_table import HashTable
from medicine import Medicine
from linear_search import linear_search

def build_data(n):
    # n unique random IDs between 1 and 10n
    ids = random.sample(range(1, 10*n), n)

    medicine_list = []  # plain one-dimensional list
    table = HashTable(2 * n) # hash table with load factor 0.5

    for product_id in ids:
        med = Medicine(product_id, f"Med{product_id}", 10.0, 50)
        medicine_list.append(med)       # add to the list
        table.insert(product_id, med)   # add to the hash table

    return medicine_list, table

if __name__ == "__main__":
    # Quick check: both structures should find the same medicine
    random.seed(42)
    med_list, table = build_data(1000)
    test_id = med_list[500].product_id
    print(linear_search(med_list, test_id))
    print(table.search(test_id))

    
