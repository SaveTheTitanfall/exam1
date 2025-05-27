import numpy as np
#1
arr1 = np.random.rand(25, 25)
print("Min:", arr1.min(), "Max:", arr1.max())
matrix_6x6 = np.zeros((6, 6), dtype=int)
np.fill_diagonal(matrix_6x6, [1, 2, 3, 4, 5, 6])
print("Matrix with diag:")
print(matrix_6x6)
mat1 = np.random.randint(0, 10, (5, 3))
mat2 = np.random.randint(0, 10, (3, 2))
product = np.dot(mat1, mat2)
print("Mult result:")
print(product)
arr2 = np.arange(1, 21)
arr2[9:16] *= -1
print("Mod arr:")
print(arr2)

# 2
x = np.arange(1, 6)
y = np.arange(6, 11)
cauchy_matrix = 1 / np.subtract.outer(x, y)
print("Cauchy mat:")
print(cauchy_matrix)
try:
    determinant = np.linalg.det(cauchy_matrix)
    print("Det:", determinant)
except np.linalg.LinAlgError:
    print("Can't calc det")
vec = np.random.rand(100)
max_idx = np.argmax(vec)
min_idx = np.argmin(vec)
print("Max idx:", max_idx, "Min idx:", min_idx)
print("Max val:", vec[max_idx], "Min val:", vec[min_idx])
