import numpy as np

np.random.seed(42)  # Reproducibility
data = np.random.rand(5, 4)
print(data)

# Extract all values from data that are greater than 0.5.
extracted_2 = [x for row in data for x in row if x > 0.5]
print("extracted : \n", extracted_2)

# Get a Boolean mask array for those same values.
mask_2 = [[True if col > 0.5 else False for col in row] for row in data]
print("mask : \n", mask_2)

# Count how many values passed the filter.
print(len(extracted_2))

# Create a copy of the original array but set all values ≤ 0.5 to 0.0.
reformatted = [[col if col > 0.5 else 0.0 for col in row] for row in data]
print("reformatted : \n", reformatted)

import numpy as np

data = np.random.rand(5, 4)
print(data)

# Get a Boolean mask array for those same values.
mask = data > 0.5
print(mask)

# Extract all values from data that are greater than 0.5.
filtered = data[mask]
print(filtered)

# Count how many values passed the filter.
print(data[mask].size)

# Create a copy of the original array but set all values ≤ 0.5 to 0.0.
# ✅ Task 4: Set all values ≤ 0.5 to 0.0 — in a copy
# np.where(condition, value_if_true, value_if_false)
reformatted_mask1 = np.where(data > 0.5, data, 0.0)
print("reformatted_mask1: \n", reformatted_mask1)
# or I can apply mask directly like so
reformatted_mask2 = np.where(mask, data, 0.0)
print("reformatted_mask2: \n", reformatted_mask2)
# 💡 What if you want to assign using a mask?
# You can do that too!
import numpy as np

np.random.seed(42)  # Reproducibility
data = np.random.rand(5, 4)
copy = data.copy()
mask = data > 0.5
copy[mask] = 42
print(copy)

# 🧙 Bonus: Fancy 2D Labeling
# Want to label the values as "High" or "Low"?

labels = np.where(data > 0.5, "High", "Low")
print(labels)
