def fibonacci_counted(n):
    # Same logic as fibonacci(n), but also counts the primitive operations
    # Returns (fibonacci value, number of calls, number of primitive operations)
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n, 1, 3          # base case: 2 comparisons + 1 return = 3 operations
    value_a, calls_a, ops_a = fibonacci_counted(n - 1)
    value_b, calls_b, ops_b = fibonacci_counted(n - 2)
    # this call: 2 comparisons, 2 subtractions, 2 calls, 1 addition, 1 return = 8 operations
    return value_a + value_b, calls_a + calls_b + 1, ops_a + ops_b + 8

    
if __name__ == "__main__":
    print(f"{'n':>3} | {'fib(n)':>8} | {'Calls':>10} | {'Operations':>11} | {'2^n':>13} | {'Growth':>6}")
    print("-" * 66)
    previous_ops = None
    for n in range(20, 31):
        value, calls, ops = fibonacci_counted(n)
        if previous_ops is None:
            growth = "-"
        else:
            growth = f"x{ops / previous_ops:.3f}"
        print(f"{n:>3} | {value:>8,} | {calls:>10,} | {ops:>11,} | {2 ** n:>13,} | {growth:>6}")
        previous_ops = ops
