# 🧮 Step 5: Transpose and Matrix Multiplication in NumPy
# Let’s compare how NumPy makes your life infinitely easier than our hand-rolled version.

# 🔄 Transpose
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print("Original:\n", a)
print("Transposed:\n", a.T)

# .T is just a property — no function call.

# Shape flips from (2, 3) → (3, 2)

# ✖️ Matrix Multiplication
# Let’s multiply two compatible matrices:
A = np.array([[1, 1, 1], [2, 2, 2]])
B = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

result = A @ B
print("Result of A @ B:\n", result)
# Or, if you want the long version:
result = np.dot(A, B)
# Same output. Just cleaner.

# Challenge 1 -
# Can you write a NumPy version of your earlier matrix_multiply(A, B) function using
# only:
# Input validation (check shape),
# @ or np.dot,
# Optional: show how A.T @ A looks?
# It’ll cement how much leaner NumPy makes this whole process. Then, if you're up for
# it, we can quickly demo how it ties into ML pipelines (like computing predictions or
# cost functions).
import numpy as np


def matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    if A.shape[1] != B.shape[0]:
        raise ValueError("Matrices dimensions do not align")
    return np.dot(A, B)  # or return A @ B


A = np.array([[1, 1, 1], [2, 2, 2]])
B = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(matrix_multiply(A, B))
print(matrix_multiply(A.T, A))

# Feedback
# ✅ Your Function Does It All:
# Type-safe input (np.ndarray) — bonus points
# Shape validation before computation
# Delegates multiplication to optimized, native C-backed np.dot
# Returns result as an ndarray, ready for downstream ML use
# This is what production-ready utility functions look like. You're already building your
# ML toolkit.

# 🧠 Stretch Thought: Use the @ Operator?
# This is identical in output, and a little more expressive:
A @ B

# That @ operator was added in Python 3.5 just for matrix math readability.
# Use whichever you find clearer — both are industry standard.

# 🌊 Bonus Challenge (Optional, for fun):
# Wanna warm up a bit of real ML logic?

# Try:
# Simulate input features (2 samples, 3 features)
X = np.array([[1, 2, 3], [4, 5, 6]])

# Simulate weights (3 features, 1 output)
W = np.array([[0.1], [0.2], [0.3]])

# Simulate the bias term
b = np.array([[1]])

# Compute predictions: Y = XW + b
Y = X @ W + b
print("Predictions:\n", Y)

Y = X @ W + 1
print("Predictions:\n", Y)
