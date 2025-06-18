def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    """creates the inverse of a matrix"""
    a, b = matrix[0]
    c, d = matrix[1]
    det = a * d - b * c
    if det == 0:
        return None
    return [[d / det, -b / det], [-c / det, a / det]]


matrix = [[1.0, 2.0], [3.0, 4.0]]
print(inverse_2x2(matrix))
