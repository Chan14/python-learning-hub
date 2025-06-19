# ✅ Step 1: NumPy Baseline
# Here’s how to compute the inverse of a 3×3 matrix using numpy.linalg.inv.
# We'll start with a test matrix you can safely invert and use to verify your
# from-scratch implementation later.
import numpy as np

# Define a 3×3 matrix (must be invertible)
A = np.array([[4, 7, 2], [3, 6, 1], [2, 5, 1]], dtype=float)

# Compute its inverse
A_inv = np.linalg.inv(A)

# Display the inverse
print("Inverse using NumPy:")
print(A_inv)

# Verify: A @ A_inv ≈ Identity matrix
identity_check = A @ A_inv
# print(np.round(identity_check, decimals=10))
print("\nA × A_inv:")
print(identity_check)
print(np.allclose(A @ A_inv, np.eye(3)))


# ✅ Full Working Version (Index-Based, No Slicing)
def determinant(matrix: list[list[float]]) -> float:
    if len(matrix) != 3 or len(matrix[0]) != 3:
        raise ValueError("Matrix must be 3x3")
    n = 3
    det = 0
    for j in range(n):
        j1, j2 = (j + 1) % n, (j + 2) % n
        j1, j2 = min(j1, j2), max(j1, j2)
        # Assign elements of the minor
        a = matrix[1][j1]
        b = matrix[1][j2]
        c = matrix[2][j1]
        d = matrix[2][j2]
        minor_det = a * d - b * c
        sign = (-1) ** j
        det += sign * matrix[0][j] * minor_det
    return det


def determinant_3x3(m):
    def det_2x2(sub):
        return sub[0][0] * sub[1][1] - sub[0][1] * sub[1][0]

    det = 0
    for j in range(3):
        # Create the 2×2 minor by excluding row 0 and column j
        minor = [[m[i][k] for k in range(3) if k != j] for i in range(1, 3)]
        cofactor = ((-1) ** j) * m[0][j] * det_2x2(minor)
        det += cofactor
    return det


A = [[4, 7, 2], [3, 6, 1], [2, 5, 1]]

# print(determinant_3x3(A))  # Should give non-zero result (→ matrix is invertible)
# print(determinant(A))


def minor(matrix: list[list[float]], i, j) -> list[list[float]]:
    return [[matrix[r][c] for c in range(3) if c != j] for r in range(3) if r != i]


def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def matrix_of_minors(matrix: list[list[float]]) -> list[list[float]]:

    return [[determinant_2x2(minor(matrix, i, j)) for j in range(3)] for i in range(3)]


def cofactor_matrix(minors: list[list[float]]) -> list[list[float]]:
    return [[(-1) ** (i + j) * minors[i][j] for j in range(3)] for i in range(3)]


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*matrix)]


A = [[4, 7, 2], [3, 6, 1], [2, 5, 1]]
det = determinant_3x3(A)
minors = matrix_of_minors(A)
cofactors = cofactor_matrix(minors)
adjugate = transpose(cofactors)
inverse = [[round(val / det, 8) for val in row] for row in adjugate]
print(inverse)

identity = np.dot(np.array(A), np.array(inverse))
print(np.round(identity, 6))  # Should be close to the identity matrix


# 💎 Full Inverse Function (No NumPy Used)
def invert_matrix_3x3(matrix: list[list[float]]) -> list[list[float]]:
    def determinant_2x2(m):
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    def minor(matrix, i, j):
        return [[matrix[r][c] for c in range(3) if c != j] for r in range(3) if r != i]

    def matrix_of_minors(matrix):
        return [
            [determinant_2x2(minor(matrix, i, j)) for j in range(3)] for i in range(3)
        ]

    def cofactor_matrix(minors):
        return [[(-1) ** (i + j) * minors[i][j] for j in range(3)] for i in range(3)]

    def transpose(matrix):
        return [list(row) for row in zip(*matrix)]

    def scale_matrix(matrix, scalar):
        return [[round(val * scalar, 8) for val in row] for row in matrix]

    # Step 1: Determinant
    det = 0
    for j in range(3):
        minor_det = determinant_2x2(minor(matrix, 0, j))
        sign = (-1) ** j
        det += sign * matrix[0][j] * minor_det

    if det == 0:
        raise ValueError("Matrix is not invertible (determinant is 0)")

    # Step 2: Inversion pipeline
    minors = matrix_of_minors(matrix)
    cofactors = cofactor_matrix(minors)
    adjugate = transpose(cofactors)
    inverse = scale_matrix(adjugate, 1 / det)

    return inverse


# ✅ Usage
A = [[4, 7, 2], [3, 6, 1], [2, 5, 1]]

inv = invert_matrix_3x3(A)

for row in inv:
    print(row)

# 🧪 Bonus: Validation with NumPy
import numpy as np

print("Is close to NumPy inverse?", np.allclose(inv, np.linalg.inv(np.array(A))))
