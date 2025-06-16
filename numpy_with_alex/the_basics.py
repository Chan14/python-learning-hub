import numpy as np

# print(np.__version__)

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))
# print(arr.dtype)
# print(arr.shape)
# print(arr.ndim)

# arr2 = np.array([[1], [2], [3], [4], [5]])
# print(arr2)

# arr3 = np.reshape(arr, (5, 1))
# print(arr3)

# arr4 = arr[:, np.newaxis]
# print(arr4)

# arr2 = np.array([1, 2, 3, 4, 5, 6])
# arr5 = arr[2:, np.newaxis]
# print(f"arr5 = \n {arr5}")

arr = np.arange(6)  # [0 1 2 3 4 5]

# reshape into 2x3
a = arr.reshape(2, 3)

# reshape into 3x2
b = arr.reshape(3, 2)

# Try adding axes:
col_vector = arr[:, np.newaxis]
row_vector = arr[np.newaxis, :]

print("2x3:\n", a)
print("3x2:\n", b)
print("Col vector shape:", col_vector.shape)
print("Row vector shape:", row_vector.shape)

import numpy as np

a = np.zeros((2, 3))
b = np.ones((2, 3))
c = np.full((2, 2), 7)

print("Zeros:\n", a)
print("Ones:\n", b)
print("Full of 7s:\n", c)

# 🧪 Your Turn!
# Write code to create:
# A 4x4 array of all zeroes
# A 2x5 array of all ones
# A 3x3 array filled with π (use np.pi)
# Then print their .dtype and .shape for each. (Watch what dtype gets chosen when
# using np.pi.)

import numpy as np

a = np.zeros((4, 4))
b = np.ones((2, 5), dtype=np.int32)
c = np.full((3, 3), np.pi)

print(
    f"4 by 4 array of zero's: dtype - {a.dtype}, shape - {a.shape}, representation - \n{a}"
)
print(
    f"2 by 5 array of one's: dtype - {b.dtype}, shape - {b.shape}, representation - \n{b}"
)
print(
    f"3 by 3 array of pi: dtype - {c.dtype}, shape - {c.shape}, representation - \n{c}"
)

# arr = np.array([[2, 3], [4, 5]])
# print(arr)

import matplotlib.pyplot as plt
import numpy as np

odds = np.arange(1, 20, 2)
points = np.linspace(-2 * np.pi, 2 * np.pi, 100)

print(f"odds: dtype - {odds.dtype}, shape - {odds.shape}, representation - \n{odds}")
print(
    f"points: dtype - {points.dtype}, shape - {points.shape}, representation - \n{points}"
)

# plot the sine curve over the second array
# y values for the points
y = np.sin(points)

plt.plot(points, y, label="sin(x)")

plt.title("Sine curve over points")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.legend()
plt.show()
