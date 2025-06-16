# 🚀 Up Next: Part 3 – Array Math & Broadcasting
# This is where NumPy transcends Python lists. You’ll learn:
# Elementwise math: +, -, *, /, **
# Matrix multiplication: @, .dot()
# Broadcasting: the magic sauce that makes shapes "stretch"
# Useful stats: .mean(), .sum(), .std(), .argmax(), etc.
# All of it will be hands-on — you'll calculate, reshape, compare, and visualize some steps.

import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print("a:", a)
print("b:", b)
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)
print("a ** 2:", a**2)


import numpy as np

col = np.array([[1], [2], [3]])  # shape (3, 1)
row = np.array([[10, 20, 30]])  # shape (1, 3)

result = col + row
print("Result:\n", result)
print("Shape:", result.shape)

import numpy as np

col = np.array([[100], [200], [300]])  # (3,1)
row = np.array([[1, 2, 3, 4]])  # (1, 4)

result = col * row  # (3, 4)
print("Result:\n", result)
print("Shape:", result.shape)

# import numpy as np

# a = np.ones((3, 2))
# b = np.ones((2, 3))

# print(a + b)  # 💣

import numpy as np

data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]])
print(data, data.shape, data.ndim)
col_min = data.min(axis=0, keepdims=True)  # shape (3,)
print(col_min, col_min.shape, col_min.ndim)
col_max = data.max(axis=0)  # shape (3,)
print(col_max, col_max.shape, col_max.ndim)
range_ = col_max - col_min  # shape (3,)
print(range_, range_.shape, range_.ndim)
normalized = (data - col_min) / range_
print(normalized)

import numpy as np

data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]])
print(data, data.shape, data.ndim)
row_min = data.min(axis=1, keepdims=True)  # shape (4,)
print(row_min, row_min.shape, row_min.ndim)
row_max = data.max(axis=1, keepdims=True)  # shape (4,)
print(row_max, row_max.shape, row_max.ndim)
range_ = row_max - row_min  # shape (3,)
print(range_, range_.shape, range_.ndim)
broadcasted = data - row_min
print(broadcasted)
normalized = (data - row_min) / range_
print(normalized)
