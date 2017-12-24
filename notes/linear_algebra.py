# linalg is module of NumPy library which contains most frequently used linear algebra operations.
import numpy.linalg as alg
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Get inversion of the matrix:
print(alg.inv(matrix))

# Get determinant of the matrix:
print(alg.det(matrix))

# Get determinant of the matrix:
print(alg.det(matrix))

# Get trace of the matrix:
print(np.trace(matrix))

# Get norm of the matrix:
print(alg.norm(matrix))

# Get norm of the matrix:
print(alg.norm(matrix))

# Get norm of the matrix:
equation = np.array([[1, 3], [4, 8]])
results = np.array([1, -2])
print(alg.solve(equation, results))

# Matrix decompositions
matrix = np.array([[10, -10, 3], [4, 5, 10], [100, 8, 9]])
q, r = alg.qr(matrix)
print(q, '\n')
print(r, '\n')
U, s, V = alg.svd(matrix)
print(U, '\n')
print(s, '\n')
print(V, '\n')

# Random numbers generation:
# Generate matrix of random numbers from range <0,1>
matrix = np.random.rand(5, 5)
print(matrix)
# Generate matrix of random numbers from a univariate "normal" (Gaussian) distribution of mean 0 and variance 1
matrix = np.random.randn(5, 5)
print(matrix)
# Generate matrix of random values from range <0,5) with size 5x5
matrix = np.random.randint(5, size=(5, 5))
print(matrix)
# Generate matrix of random values from range <5,10) with size 5x5
matrix = np.random.randint(5, size=(5, 5)) + 5
print(matrix)
# Get 3 random elements from range <0,5)
matrix = np.random.choice(5, 3)
print(matrix)

# Distributions:
# Draws samples from exponential distribution
matrix = np.random.exponential(5, 3)
print(matrix)
# Draws samples from geometric distribution
matrix = np.random.geometric(1, 3)
print(matrix)
# Draws samples from normal distribution
matrix = np.random.normal(5, 3)
print(matrix)
# Draws samples from poisson distribution
matrix = np.random.poisson(5, 3)
print(matrix)

# Statistics:
matrix = np.random.randint(5, size=(5, 5)) + 5
print(matrix)
# Maximum value
print(matrix.max())
# Minimum value
print(matrix.min())
# Sum of values
print(matrix.sum())
# Mean of values
print(matrix.mean())
# Median of values
print(np.median(matrix))
# Standard deviation of values
print(matrix.std())
# Variance of values
print(matrix.var())
# Covariance of values
print(np.cov(matrix))

# Sorting / searching
matrix = np.random.randint(5, size=(5, 5)) + 5
# Normal sorting
print(np.sort(matrix))
# Sorting with specified algorithm - returns sorted matrix
print(np.sort(matrix, kind='quicksort'))
# Sorting with specified algorithm - returns indexes of elements from input matrix
print(np.argsort(matrix, kind='quicksort'))
# Get index of maximum element in matrix:
print(np.argmax(matrix))
# Get index of minimum element in matrix:
print(np.argmax(matrix))
# Get indexes of elements which satisfy given predicate:
print(np.argwhere(matrix == 9))
# Get elements which satisfy given predicate:
print(np.where(matrix == 9))

# File operations
matrix = np.random.rand(5, 5)
# Save matrix to the file:
# np.savetxt('example', matrix)
# Load matrix from the file:
# matrix = np.loadtxt('example')
# print(matrix)
