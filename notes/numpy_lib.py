import numpy as np

# Create matrix using numpy:
# Single dimensional matrix:
matrix_1D = np.array([0, 1])
print(matrix_1D)

# Multi dimensional matrix:
matrix_2D = np.array([[0, 1], [2, 3]])
print(matrix_2D)
matrix_3D = np.array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
print(matrix_3D)
# etc..

# Matrix of specified type: ie complex numbers:
matrix_complex = np.array([1, 2, 3], dtype=complex)
print(matrix_complex)

# Create single dimensional array (vector) of numbers from given range with specified step:
vector = np.arange(0, 10, 2)
print(vector)

# Create vector with given number of elements distributed over specified range
# with regular spaces (linear incrementation within given range):
lin_range = np.linspace(1, 4, 4)
print(lin_range)

# Matrix fulfilled with 1: (n,m) where n is number of rows and m number of cols
ones_matrix = np.ones((2, 3))
print(ones_matrix)

# Matrix fulfilled with 0: (n,m) where n is number of rows and , is the number of cols
zeros_matrix = np.zeros((2, 3))
print(zeros_matrix)

# Square matrix where n is the size of rows/cols with ones at it's diagonal
eye_matrix = np.eye(4)
print(eye_matrix)

# It is possible to change the size of already created matrix by using reshape method:
any_array = np.arange(1, 5, 1)
print(any_array)
print(any_array.reshape(4, 1))

# Ways to resize matrix:
# 1. Resize the original matrix:
matrix = np.array([1, 2, 3])
print(matrix)
matrix.resize(3, 1)
print(matrix)
# 2. Return resized copy of matrix (without modifying the original):
print(matrix.reshape(1, 3))

# Accessing elements of matrix by indexes:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
# Get first row:
print(matrix[0])
# Get first col:
print(matrix[:, 0])
# Generally it's possible to extract submatrix from matrix using standard python way: (start:stop:step)
print(matrix[::, ::])

# Ways to get size of matrix:
# Get number of elements:
print(matrix.size)
# Get number of rows:
print(matrix[:, 0].size)
# Get number of cols:
print(matrix[0].size)

# Transpose matrix:
print(np.transpose(matrix))

# Flatten matrix to vector
print(matrix.ravel())
print(matrix.reshape(-1))

# Adding/deleting elements:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
# Insert new row on the first position and flatten matrix to vector:
print(np.insert(matrix, 1, [11, 22, 33]))
# Insert new row on the first position
print(np.insert(matrix, 1, [11, 22, 33], axis=0))
# Insert new col on the first position
print(np.insert(matrix, 1, [11, 22, 33], axis=1))
# Append (insert as the last element) passed matrix (sizes of inserted and target matrices must be the same)
print(np.append(matrix, [[11, 22, 33]], axis=0))
# Delete row under 1 index from the matrix:
print(np.delete(matrix, 1, axis=0))
# Delete col under 1 index from the matrix:
print(np.delete(matrix, 1, axis=1))
# Delete rows under given indexes:
print(np.delete(matrix, [0, 2], axis=0))
# Delete cols under given indexes:
print(np.delete(matrix, [1, 2], axis=1))

# Adding or subtracting matrices:
matrix_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1)
print(matrix_2)
# Subtract two matrices
print(matrix_1 - matrix_2)
print(np.subtract(matrix_1, matrix_2))
# Add two matrices
print(matrix_1 + matrix_2)
print(np.add(matrix_1, matrix_2))
# Add single value to all elements from matrix
print(matrix_1 + 1)
# Add single value to all elements from matrix
print(matrix_1 - 1)

# Matrix multiplication:
matrix_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Multiply each element by single value:
print(matrix_1 * 2)
# Dot product for two matrices - matrices multiplication:
print(matrix_1, '\n')
print(matrix_2, '\n')
print(np.dot(matrix_1, matrix_2))

# Matrix raised to the power of n
# Traditional way
print(matrix_1 ** 2)
# Using NumPy
print(np.power(matrix_1, 2))

# Comparison of matrices:
matrix_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Compare each element
print(matrix_1 < matrix_2)
print(matrix_1 == matrix_2)
print(matrix_1 > matrix_2)

# Verify if all/any of elements are true for the given predicate:
print(np.all(matrix_1 <= matrix_2))
print(np.any(matrix_1 <= matrix_2))

# Divide and concatenate matrices:
matrix_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Concatenate two matrices (add new rows):
print(np.concatenate((matrix_1, matrix_2)))
print(np.concatenate((matrix_1, matrix_2), axis=0))
# Concatenate two matrices (add new cols):
print(np.concatenate((matrix_1, matrix_2), axis=1))
# Concatenate vertically
print(np.vstack((matrix_1, matrix_2)))
# Concatenate horizontally
print(np.hstack((matrix_1, matrix_2)))
# Split matrix horizontally:
# Into 3 equal pieces
print(np.hsplit(matrix_1, 3))
# Over specified indexes: 0, n1, n2 ,..., nk, length-1
print(np.hsplit(matrix_1, [1, 3]))
# Split matrix vertically:
# Into 3 equal pieces
print(np.vsplit(matrix_1, 3))
# Over specified indexes: 0, n1, n2 ,..., nk, length-1
print(np.vsplit(matrix_1, [1, 3]))