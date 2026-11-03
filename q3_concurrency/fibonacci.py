def fibonacci(n):
    # Recursive definition: fib(0) = 0, fib(1) = 1, fib(n) = fib(n - 1) + fib(n - 2)
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:                                   # base case: 2 comparisons
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # 2 subtractions, 2 calls, 1 addition


if __name__ == "__main__":
    # Quick check against known values
    for n in [0, 1, 2, 5, 10, 20]:
        print(f"fib({n}) = {fibonacci(n)}")
