A = [1, 2, 3, 4, 5]
print([x for x in A])

B = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print([y for y in [x for x in B]])


print([A[i] for i in range(len(A))])
result = [[0] * len(B[0]) for x in B]
print(result)
result = [[B[i][j] for j in range(len(B[i]))] for i in range(len(B))]
print(result)

# Transpose
B = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
result = [[0] * len(B) for x in B[0]]
print(result)
result = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]
print(result)
