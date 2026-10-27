import random
import time
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

def measure(n):
    # Build n records and time the average search in each structure
    med_list, table = build_data(n)

    all_ids = []
    for med in med_list:
        all_ids.append(med.product_id)

    targets = random.sample(all_ids, 1000)

    start = time.perf_counter_ns()
    for target in targets:
        linear_search(med_list, target)
    end = time.perf_counter_ns()
    list_avg = (end - start) / len(targets)

    start = time.perf_counter_ns()
    for target in targets:
        table.search(target)
    end = time.perf_counter_ns()
    hash_avg = (end - start) / len(targets)

    return list_avg, hash_avg



if __name__ == "__main__":
    # Quick check: both structures should find the same medicine
    random.seed(42)

    print(f"{'Records':>9} {'List (ns)':>14} {'Hash(ns)':>12} {'Faster by':>11}")
    print("-" * 50)


    for n in [1000, 10000, 100000]:
        list_avg, hash_avg = measure(n)
        speedup = list_avg / hash_avg
        print(f"{n:>9,} {list_avg:>14,.0f} {hash_avg:>12,.0f} {speedup:>10.1f}x") 
    
