# plotter.py

import matplotlib.pyplot as plt


# Plot results
def plot_results(task_labels, avg_times_ms):
    plt.figure(figsize=(8, 5))
    plt.bar(task_labels, avg_times_ms, color="skyblue")
    plt.title("Benchmark Results")
    plt.ylabel("Average Time (ms)")
    plt.xlabel("Tasks")
    plt.grid(True, axis="y", linestyle="--", alpha=0.7)
    for i, v in enumerate(avg_times_ms):
        plt.text(i, v + 1, f"{v:.2f}", ha="center")
    plt.tight_layout()
    plt.show()
