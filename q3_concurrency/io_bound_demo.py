import threading
import time

WAIT_TIMES = [1, 1, 1]   # seconds each task waits (like a download or reading a file)


def wait_task(seconds):
    # Simulates an I/O task: the thread is waiting, not using the CPU
    time.sleep(seconds)


def run_with_threads():
    start = time.perf_counter_ns()
    threads = []
    for seconds in WAIT_TIMES:
        thread = threading.Thread(target=wait_task, args=(seconds,))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return time.perf_counter_ns() - start


def run_without_threads():
    start = time.perf_counter_ns()
    for seconds in WAIT_TIMES:
        wait_task(seconds)
    return time.perf_counter_ns() - start


if __name__ == "__main__":
    threaded_time = run_with_threads()
    sequential_time = run_without_threads()
    print("I/O-bound tasks (3 tasks, each waits 1 second):")
    print(f"With threads   : {threaded_time / 1_000_000_000:.3f} seconds")
    print(f"Without threads: {sequential_time / 1_000_000_000:.3f} seconds")
