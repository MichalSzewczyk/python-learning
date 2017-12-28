import numpy as np
import numpy.random as ran
import matplotlib.pyplot as plt
from scipy import misc

# exercise 1
random_matrix = ran.rand(1, 10000)
print(random_matrix)
random_matrix += 1
print(random_matrix)

# exercise 2
random_matrix = ran.rand(1, 10000)
from math import sin, cos

result = np.sin(random_matrix) + np.cos(random_matrix)
print(result)


# exercise 3
def cube_sum(x):
    """Zwraca sume szescianow elementow"""
    result = 0
    for i in range(len(x)):
        result += x[i] ** 3
    return result


def almost_variance(x):
    """Oblicza 1/n * SUM (x_i - mean(x))^4"""
    m = sum(x) / len(x)
    result = 0
    for i in range(len(x)):
        result += (x[i] - m) ** 4
    result /= len(x)
    return result


def cube_sum_faster(x):
    """Zwraca sume szescianow elementow"""
    return np.sum(np.array(x) ** 3)


def almost_variance_faster(x):
    """Oblicza 1/n * SUM (x_i - mean(x))^4"""
    return np.sum((x - np.mean(x)) ** 4) / len(x)


matrix = ran.random((1, 10))
print(matrix)
print(cube_sum_faster(matrix))
print(cube_sum(matrix))
print(almost_variance_faster(matrix))
print(almost_variance(matrix))


# exercise 4
def broadcast(v_size):
    return np.arange(v_size) * np.arange(v_size).reshape(v_size, 1)


print(broadcast(10))


# exercise 5
# def euclid(m, point_x, point_y):
#     return np.linalg.norm(m[point_x], m[point_y], axis=1)
#
#
# print(euclid(np.random.rand(10, 5), 0, 1))

# exercise 6
def whitening(m):
    return (m - np.mean(m, axis=0)) / np.std(m, axis=0)


matrix = np.arange(0, 10).reshape(5, 2)
print(matrix)
print(whitening(matrix))


# exercise 7
def closest(m, x):
    return m[np.argmin(np.abs(m - x))]


print(closest(np.array([1, -4, 3]), 1.5))


# exercise 8
def compute(x, a):
    return np.sum(a * np.insert(np.cumprod(np.linspace(x, x, a.size - 1)), 0, values=[1]))


matrix = np.array([1, 2, 3])
print(compute(5, matrix))

# exercise 9
# matrix = misc.imread('img.png')
# f = misc.face()
# print(plt.imshow(f))
# plt.show()
face = misc.imread('img.png')