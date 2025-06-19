# 🧩 Challenge 2: NumPy Slicing and Reshaping
# We're shifting into NumPy now. I want you to imagine you're working with an image —
# a 3D NumPy array shaped (3, 4, 3):
# 3 "rows" (could be height),
# 4 "columns" (could be width),
# 3 channels (e.g., RGB).
# 🐍 Code Setup
# import numpy as np

# image = np.arange(3 * 4 * 3).reshape(3, 4, 3)
# print(image)
# Inspect it by printing, and you'll see something like this:
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]
#   [ 9 10 11]]

#  [[12 13 14]
#   [15 16 17]
#   [18 19 20]
#   [21 22 23]]

#  [[24 25 26]
#   [27 28 29]
#   [30 31 32]
#   [33 34 35]]]

# 🎯 Your Tasks:
# Extract the red channel (i.e. all [ :, :, 0 ]) — shape should be (3, 4)
# Flatten the entire image into a 1D array.
# Reshape the image into shape (4, 3, 3) — i.e. swap height and width.
# Reverse the pixel order along the width axis (axis=1).
import numpy as np

image = np.arange(3 * 4 * 3).reshape(3, 4, 3)
print(image)
print("Slice:\n", image[:, :, 0])
flattened = [channel for row in image for pixel in row for channel in pixel]
print(flattened)
reshaped_image = image.reshape((4, 3, 3))
print("Reshaped image : \n", reshaped_image)
reversed_image = image[:, ::-1, :]
print("Reversed image : \n", reversed_image)
print("Horizontally flipped image (axis=1):\n", image[:, ::-1, :])
# 💡 Bonus Tip: Alternative using np.flip
reversed_image = np.flip(image, axis=1)  # flips along width
# But the slicing ([::-1]) method is both faster and more Pythonic in most cases — and gives you
# tighter control.
# Improved
import numpy as np

image = np.arange(3 * 4 * 3).reshape(3, 4, 3)
print(image)
flattened = image.flatten()
# print(flattened)
flattened_2 = image.ravel()  # slightly faster, returns a view if possible
flattened_3 = image.reshape(-1)
print(flattened_2)
flattened_2[0] = 49
print(image)


import numpy as np

B = np.array([[1, 2, 3], [4, 5, 6]])
print(B)
print(B[:-1])
print(B[:, :-1])
print(B[:-1, :])
print(B[::-1])
