# 🧠 Challenge: The Matrix Detective
# You’re given a list of 3 vectors in 3D space.
# Each vector is represented as a list of 3 numbers.
# vectors = [
#     [2, 4, 6],
#     [1, 2, 3],
#     [0, 1, -1]
# ]

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(len(list1))


def _valid_3x3_matrix(matrix: list) -> bool:
    if not matrix:
        return False
    if len(matrix) != 3:
        return False
    for i in range(3):
        if len(matrix[i]) != 3:
            return False
    return True


def calculate_determinant(matrix: list) -> int:
    if not _valid_3x3_matrix(matrix):
        raise ValueError("Input must be a 3x3 matrix represented as a list of 3 lists.")
    outer_js = [1, 0, 0]
    inner_js = [2, 2, 1]
    signs = [1, -1, 1]
    det = 0
    for i in range(3):
        det += (
            signs[i]
            * matrix[0][i]
            * (
                matrix[1][outer_js[i]] * matrix[2][inner_js[i]]
                - matrix[1][inner_js[i]] * matrix[2][outer_js[i]]
            )
        )
    return det


print(calculate_determinant(list1))
