# benchmark.py
import time


# Warmup function
def _warmup(task, warmup_iterations):
    for _ in range(warmup_iterations):
        task()


# Benchmark function
def benchmark(tasks, iterations, warmup_iterations):
    results = []
    for idx, task in enumerate(tasks):
        _warmup(task, warmup_iterations)
        total_ns = 0
        for _ in range(iterations):
            start_ns = time.perf_counter_ns()
            task()
            end_ns = time.perf_counter_ns()
            total_ns += end_ns - start_ns
        avg_ms = total_ns / iterations / 1e6
        print(f"Task {idx} average time: {avg_ms:.3f} ms")
        results.append(avg_ms)
    return results
