import numpy as np

# 🔰 Step 1: Create and Inspect a NumPy Array
# Create a basic 2D array

a = np.array([[1, 2], [3, 4]])
print(a)


# Get basic info
print("Shape : ", a.shape)  # (2, 2)
print("Number of dimensions : ", a.ndim)  # 2
print("Data type : ", a.dtype)  # int64
print("Size (total elements) :", a.size)  # 4

# 🔧 Step 2: Common Array Constructors
import numpy as np

print(np.zeros((3, 4)))  # 3x4 matrix of 0s
print(np.ones((2, 2)))  # 2x2 matrix of 1s
print(np.eye(3))  # Identity matrix
print(np.arange(10))  # [0, 1, ..., 9]
print(np.linspace(0, 1, 5))  # 5 evenly spaced numbers between 0 and 1

import numpy as np

print("Zeros (3x4):\n", np.zeros((3, 4)))
print("Ones (2x2):\n", np.ones((2, 2)))
print("Identity (3x3):\n", np.eye(3))
print("Arange 0-9:\n", np.arange(10))
print("Linspace 0 to 1 (5 points):\n", np.linspace(0, 1, 5))

# 🪓 Step 3: Indexing & Slicing
import numpy as np

a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Access a single element (row 1, col 2)
print("a[1, 2] =", a[1, 2])  # 60
# Get a full row
print("Row 0:", a[0])  # [10 20 30]
# Get a full column
print("Col 1:", a[:, 1])  # [20 50 80]
# Slice a submatrix (rows 0-1, cols 1-2)
print("Slice:\n", a[:2, 1:3])
print("Slice:\n", a[0:2, 1:3])
