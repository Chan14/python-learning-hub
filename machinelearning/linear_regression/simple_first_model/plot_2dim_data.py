import matplotlib.pyplot as plt
import numpy as np


def plot_data(x, y, xlabel, ylabel, title):
    """
    Plot 2D scatter data.
    """
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color="blue", marker="o", label="Data")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_data_and_model(x, y, y_pred, xlabel, ylabel, title, pred_label):
    """
    Plot 2D data and prediction line.
    """
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color="blue", marker="o", label="Data")

    # Sort for clean line plotting
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_pred_sorted = y_pred[sorted_indices]

    plt.plot(x_sorted, y_pred_sorted, color="red", label=pred_label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
