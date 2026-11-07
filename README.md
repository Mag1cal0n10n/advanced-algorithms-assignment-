# advanced-algorithms-assignment-

5022CMD Advanced Algorithms portfolio. Three questions, one folder each.

## Requirements
- Python 3.10 or newer (tested on Python 3.14)
- Standard library only, nothing to install

## How to run
Open a terminal in the repo folder, then run the file you want:

```
python q1_hashing/inventory_system.py
```

## Q1 – Hashing (Pharmacy Inventory)
| File | What it does |
|---|---|
| `inventory_system.py` | **Main program.** Menu to insert, search, edit, delete and display medicines. Search shows the time for the hash table and the array. |
| `performance_test.py` | Experiment: average search time, hash table vs array, for 1,000 / 10,000 / 100,000 records. |
| `hash_table.py` | Hash table with open addressing and linear probing. |
| `medicine.py` | `Medicine` entity class. |
| `linear_search.py` | Linear search over a one-dimensional list. |

```
python q1_hashing/inventory_system.py
python q1_hashing/performance_test.py
```

## Q2 – Directed Graph (Course Prerequisites)
| File | What it does |
|---|---|
| `course_system.py` | **Main program.** Menu to list courses, show details, show prerequisites and unlocked courses, add a course, add or remove a prerequisite. |
| `graph.py` | Generic unweighted directed graph (adjacency list). |
| `course.py` | `Course` entity class. |

```
python q2_graph/course_system.py
```

## Q3 – Concurrency (Fibonacci with Threads)
| File | What it does |
|---|---|
| `threading_test.py` | **Main experiment.** Fib(35), Fib(38), Fib(40) with and without multithreading, 10 rounds each, times in nanoseconds. Takes a few minutes. |
| `operation_count.py` | Counts calls and primitive operations to show O(2^n) growth. |
| `io_bound_demo.py` | Shows threads do help when tasks are waiting (I/O-bound). |
| `fibonacci.py` | Recursive Fibonacci function. |

```
python q3_concurrency/threading_test.py
python q3_concurrency/operation_count.py
python q3_concurrency/io_bound_demo.py
```
