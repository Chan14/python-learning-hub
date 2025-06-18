# 🚀 Challenge: matrix_multiply(A, B)
# 🧩 Problem Statement:
# Write a function matrix_multiply(A, B) that multiplies two 2D matrices A and B and
# returns the resulting matrix.
# 📥 Input:
# A: a list of lists representing an m x n matrix
# B: a list of lists representing an n x p matrix

# 📤 Output:
# The resulting m x p matrix as a list of lists.
# ❗Constraints:
# Don’t use NumPy.
# You may use nested loops or comprehensions, whichever feels clean.
# Assume all inner lists are well-formed (no jagged edges), but dimensions must be
# validated.

# ✅ Example:
A = [
    [1, 2],
    [3, 4],
]

B = [
    [5, 6],
    [7, 8],
]

# matrix_multiply(A, B)
# → [
#     [19, 22],
#     [43, 50]
#   ]
# 🧪 Hints to Self-Check Later:
# How do you compute a single element of the result?
# What are the dimensions of the output?
# Should you transpose B to make accessing columns easier?


def matrices_valid_for_multiplication(A, B):
    return len(A[0]) == len(B)


def matrix_multiply(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    if not matrices_valid_for_multiplication(A, B):
        raise ValueError("Matrix dimensions do not align: A.columns must equal B.rows")
    rows, cols = len(A), len(B[0])
    inner_dim = len(A[0])

    # result = list([0 for x in range(cols)] for x in range(rows))
    # Cleaner and slightly more idiomatic result initialization
    result = [[0.0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            # sum = 0
            # for k in range(inner_dim):
            #     sum += A[row][k] * B[k][col]
            # result[row][col] = sum
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(inner_dim))

    return result


print(matrix_multiply(A, B))
A = [[1, 1, 1], [2, 2, 2]]
B = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
assert matrix_multiply(A, B) == [[6, 6, 6], [12, 12, 12]]
B = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
try:
    matrix_multiply(A, B)
except ValueError as e:
    print("ValueError as expected")

# 🧩 Next Challenge: matrix_transpose()
# 🧠 Problem Statement:
# Write a function matrix_transpose(matrix) that returns the transpose of a 2D list.
# 📥 Input:
# matrix: a list of m rows, each with n columns
# 📤 Output:
# Transposed matrix with n rows and m columns

# 🔄 Example:
A = [[1, 2, 3], [4, 5, 6]]

# matrix_transpose(A)
# → [
#     [1, 4],
#     [2, 5],
#     [3, 6]
#   ]


def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    input_rows, input_cols = len(matrix), len(matrix[0])
    result = [[0.0] * input_rows for x in range(input_cols)]
    for i in range(input_rows):
        for j in range(input_cols):
            result[j][i] = matrix[i][j]
    return result


print(transpose_matrix(A))
