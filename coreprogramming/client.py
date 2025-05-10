# client.py
from benchmark import benchmark, warmup
from plotter import plot_results
from prime import is_prime, is_prime_optimized_div, is_prime_optimized_mul

# Define constants
WARMUP_ITERATIONS = 3
BENCHMARK_ITERATIONS = 5
START = 100_000
END = 200_000


# Task definitions
def task0():
    for i in range(START, END + 1):
        is_prime(i)


def task1():
    for i in range(START, END + 1):
        is_prime_optimized_div(i)


def task2():
    for i in range(START, END + 1):
        is_prime_optimized_mul(i)


# Main execution
if __name__ == "__main__":
    tasks = [task0, task1, task2]
    task_labels = ["is_prime", "optimized_div", "optimized_mul"]
    avg_times = benchmark(tasks, BENCHMARK_ITERATIONS, WARMUP_ITERATIONS)

    print("\nBenchmark Results:")
    for label, time_ms in zip(task_labels, avg_times):
        print(f"{label}: {time_ms:.3f} ms")

    plot_results(task_labels, avg_times)
