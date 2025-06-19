# 🧩 Challenge 1: Matrix Transpose via List Comprehension
# You’ve already tried this but let’s revisit in a slightly clearer format.
# Transpose a 2D
# list of any dimension (not just 2x2 or 3x3). For example:

A = [[1, 2, 3], [4, 5, 6]]
# Expected output:
# [
#     [1, 4],
#     [2, 5],
#     [3, 6]
# ]

# 📝 Instructions:
# Write a one-liner list comprehension.
# No loops allowed (not even in a helper function).
# Assume all rows are of equal length.
# Give it a shot without peeking at any NumPy yet — this is to reinforce nested
# comprehension syntax. Once you’re done, I’ll give you a very cool twist on this that
# ties into NumPy vectorization.

    # 1st step transposed = [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
    transposed = [[row[j] for row in A] for j in range(len(A[0]))]
    print(transposed)
