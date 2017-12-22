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


