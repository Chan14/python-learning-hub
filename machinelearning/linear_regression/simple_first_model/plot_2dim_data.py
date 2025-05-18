import matplotlib.pyplot as plt
import numpy as np


def _plot_data(x, y, xlabel, ylabel, plot_title):
    plt.scatter(x, y, color="blue", marker="o", label="Data")
    plt.title(plot_title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def plot_data(x, y, xlabel, ylabel, plot_title):
    _plot_data(x, y, xlabel, ylabel, plot_title)
    plt.legend()
    plt.show()


def plot_data_and_model(x, y, y_pred, xlabel, ylabel, plot_title, pred_label):
    _plot_data(x, y, xlabel, ylabel, plot_title)
    # Sort x and y_pred based on ascending x for a clean line plot
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_pred_sorted = y_pred[sorted_indices]

    plt.plot(x_sorted, y_pred_sorted, color="red", label=pred_label)
    plt.legend()
    plt.show()
