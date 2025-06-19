import numpy as np

np.random.seed(42)  # Reproducibility
data = np.random.rand(5, 4)
print(data)
# # 🧠 1. .astype() — For Binary Masks or Type Conversion
# Say you want to turn a Boolean mask into 1s and 0s (often useful for loss functions,
# accuracy tracking, etc.):

mask = data > 0.5
binary_mask = mask.astype(int)
print(binary_mask)
# This is an incredibly lightweight way to convert masks into numeric arrays (can also
# convert to float, str, etc.)

# ✨ Why It’s Useful:
# You can now multiply this binary mask with something, e.g.:
# result = binary_mask.astype(float) * data
# result = np.where(data > 0.5, data, 0.0)
result = (data > 0.5).astype(float) * data
print(result)
# This gives you the same effect as np.where(data > 0.5, data, 0.0),
# but using arithmetic masking. Sometimes faster!

# 🧠 2. Broadcasting with Masks
# Let’s say you want to normalize only the values > 0.5. You can do this elegantly:
import numpy as np

np.random.seed(42)
data = np.random.rand(5, 4)
mask = data > 0.5
print(mask)

# let's make a copy
copy = data.copy()
print("copy : \n", copy)
# Subtract the mean of only the high values, but only where the mask is True
print("Original copy[mask] : \n", copy[mask])
copy[mask] = copy[mask] - np.mean(copy[mask])
print("changed copy[mask] : \n", copy[mask])
print(copy)

# 🔍 What’s Happening, Step-by-Step:
# 🟦 mask is a Boolean array:
# Same shape as copy. Let's say it's:
# [[False,  True, False],
# #  [ True, False,  True]]
# 🟦 copy[mask] (right side):
# This extracts all values from copy where mask is True.

# It's a 1D array now — e.g., [0.7, 0.9, 0.8]

# np.mean(copy[mask]) computes the mean of just those values → say 0.8.

# 🟩 The RHS becomes:
# copy[mask] - np.mean(copy[mask])
# So we’re subtracting the scalar 0.8 from the 1D masked array [0.7, 0.9, 0.8]

# NumPy broadcasts this scalar across all 3 values:
# [0.7 - 0.8, 0.9 - 0.8, 0.8 - 0.8] → [-0.1, 0.1, 0.0]

# 🟥 Now the LHS: copy[mask] = ...
# This is mask-based assignment
# You’re telling NumPy:
# “Hey, for every element in copy where the mask is True, replace the value with
# the result from the RHS.”
# The LHS copy[mask] is a reference to the locations in memory that passed the mask.
# So you're directly mutating those locations, but leaving everything else in copy
# untouched.

# 💥 Summary of Insight:
# You're not assigning to the whole array, only the masked locations.
# NumPy preserves the mask structure and slices it behind the scenes.
# Broadcasting on the RHS means you can apply scalar operations to many masked elements.
# The mask is unchanged — it's just being used as a selector.
# The original copy array is mutated in-place, but only where mask == True.

# 🔬 Analogy:
# Think of it like:
# “Take a highlighter (mask) and mark some cells in a table. Now subtract 0.8 only
# from the highlighted cells. Leave the rest untouched.”

# ✅ Final Check
# You can see this effect with a toy array:

import numpy as np

arr = np.array([0.2, 0.6, 0.9, 0.3])
mask = arr > 2
arr[mask] = arr[mask] - np.mean(arr[mask])
print(arr)  # [0.2 0.6 0.9 0.3]

# [0.2        0.6 - mean  0.9 - mean  0.3]
# The rest of the array remains untouched.

# 🧠 3. Slicing with Masks + Indices (np.where combo)
import numpy as np

np.random.seed(42)  # Reproducibility
data = np.random.rand(5, 4)
print(data)
# Sometimes you don’t want just the values — you want the indices of elements that
# match a condition.
indices = np.where(data > 0.5)
print(
    indices
)  # (array([0, 0, 0, 1, 2, 2, 2, 3, 4]), array([1, 2, 3, 3, 0, 1, 3, 0, 1]))
# This gives you: (array([...]), array([...]))
# It’s a tuple of row indices and column indices — i.e., the coordinates of True values in the mask.
# You can then do:
for i, j in zip(*indices):
    print(f"data[{i}][{j}] = {data[i][j]}")
# Or just directly:
print(data[indices])  # same as data[data > 0.5]
# print(data[data > 0.5])

# 🎓 Bonus: Combine Multiple Conditions with Masks
mask = (data > 0.3) & (data > 0.7)
print(data[mask])
# Note: Use & (bitwise AND) instead of and — NumPy overrides it for element-wise logic.

# Also:
mask = (data < 0.2) | (data > 0.8)
print(data[mask])
