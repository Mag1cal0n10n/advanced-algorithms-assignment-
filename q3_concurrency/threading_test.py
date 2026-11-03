import threading
import time
from fibonacci import fibonacci

INPUTS = [35, 38, 40]   # one Fibonacci number per task (one thread each)
ROUNDS = 10             # how many times each experiment is repeated


def worker(n, results, index):
    # Calculates fibonacci(n) and records when this task started and ended
    start = time.perf_counter_ns()
    value = fibonacci(n)
    end = time.perf_counter_ns()
    results[index] = (n, value, start, end)

def earliest_start(results):
    # Start time of the task that started first
    first_start = results[0][2]
    for n, value, start, end in results:
        if start < first_start:
            first_start = start
    return first_start

def total_time(results):
    # T = end time of the task that finished last - start time of the task that started first
    last_end = results[0][3]
    for n, value, start, end in results:
        if end > last_end:
            last_end = end
    return last_end - earliest_start(results)


def run_with_threads():
    # Step 3: one separate thread for each Fibonacci number
    results = [None] * len(INPUTS)
    threads = []
    for i in range(len(INPUTS)):
        thread = threading.Thread(target=worker, args=(INPUTS[i], results, i))
        threads.append(thread)
    for thread in threads:
        thread.start()          # start all three threads
    for thread in threads:
        thread.join()           # wait until every thread has finished
    return total_time(results), results


def run_without_threads():
    # Step 4: the same work, one after another in the main thread
    results = [None] * len(INPUTS)
    for i in range(len(INPUTS)):
        worker(INPUTS[i], results, i)
    return total_time(results), results


def format_values(results):
    # Builds the text "Fib(35)=9227465, Fib(38)=39088169, Fib(40)=102334155"
    parts = []
    for n, value, start, end in results:
        parts.append(f"Fib({n})={value}")
    return ", ".join(parts)


def run_experiment(title, run_function):
    # Runs one experiment ROUNDS times, prints T for every round, returns the average T
    print(f"\n=== Fibonacci Computation ({title}) ===")
    total = 0
    for round_number in range(1, ROUNDS + 1):
        time_taken, results = run_function()
        total += time_taken
        print(f"Round {round_number:>2}: {format_values(results)} | T = {time_taken:>14,} ns")
    average = total / ROUNDS
    print(f"Total T   ({title}): {total:,} ns")
    print(f"Average T ({title}): {average:,.0f} ns ({average / 1_000_000_000:.3f} seconds)")
    return average, results


def show_timeline(title, results):
    # Shows when each task started and finished, counted from the first start
    first_start = earliest_start(results)
    print(f"\n{title}:")
    for n, value, start, end in results:
        started = (start - first_start) / 1_000_000_000
        finished = (end - first_start) / 1_000_000_000
        print(f"  Fib({n}): started at {started:6.3f} s, finished at {finished:6.3f} s")


if __name__ == "__main__":
    threaded_avg, threaded_results = run_experiment("With Multithreading", run_with_threads)
    sequential_avg, sequential_results = run_experiment("Without Multithreading", run_without_threads)

    difference = (sequential_avg - threaded_avg) / sequential_avg * 100
    if difference > 0:
        print(f"\nObservation: Multithreading reduced the average time by {difference:.1f}%.")
    else:
        print(f"\nObservation: Multithreading did NOT reduce the time (it was {-difference:.1f}% slower).")

    # Timeline of the last round: shows the threads took turns because of the GIL
    show_timeline("Last round WITH multithreading", threaded_results)
    show_timeline("Last round WITHOUT multithreading", sequential_results)
