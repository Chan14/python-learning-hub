A = [1, 2, 3, 4, 5]
B = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

A2 = [x for x in A]
print(A2)
B2 = [[j for j in i] for i in B]
print(B2)

# index based
A = [1, 2, 3, 4, 5]
B = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
A3 = [A[i] for i in range(len(A))]
print(A3)
B3 = [[B[i][j] for j in range(len(B[i]))] for i in range(len(B))]
print(B3)

# Transpose using plain Python - dont use Numpy
A = [1, 2, 3, 4, 5]
A4 = [[A[i]] for i in range(len(A))]
print(A4)
B = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
B4 = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]
print(B4)
B4 = [[j[i] for j in B] for i in range(len(B[0]))]
print(B4)
