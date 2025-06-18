# 🔮 Step 4: Broadcasting
# Broadcasting is NumPy’s way of handling arithmetic between arrays of different shapes without explicit loops. It automagically stretches smaller arrays to match the shape of larger ones — if they’re compatible.

# ⚙️ Example 1: Scalar + Array
import numpy as np

a = np.array([1, 2, 3])
print(a + 10)  # [11 12 13]
# NumPy "broadcasts" the 10 to all elements in a. No loops. No drama.

# ⚙️ Example 2: 2D + 1D
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

b = np.array([10, 20, 30])

print(a + b)
# 📌 What's happening here?
# Shape of a: (2, 3)
# Shape of b: (3,)
# NumPy stretches b across rows to match a.

# 🚨 Rules of Broadcasting
# NumPy compares shapes from the end, dimension by dimension:
# If dimensions are equal → OK
# If one is 1 → it gets stretched (broadcast)
# If neither matches → 💥 Error
# ⚠️ Incompatible Example
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([10, 20, 30])
print(a + b)  # 🚫 ValueError
# Because:
# a: (2, 2)
# b: (3,) → can't align to 2 columns
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[10], [20]])  # Column vector

print("a:\n", a)
print("b:\n", b)
print("a + b:\n", a + b)

# This time, you’re adding a column vector — b gets broadcast across columns.
