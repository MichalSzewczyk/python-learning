import random

import numpy
import numpy as np
import time


# zad 1
def array():
    rand_arr = []
    for i in range(10000):
        rand_arr.append(random.randint(0, 1))
    start = time.time()
    for i in rand_arr:
        i += 1
    print('array: ' + str(time.time() - start))


def numpy_array():
    rand_arr = np.array([])
    for i in range(10000):
        numpy.append(rand_arr, (random.randint(0, 1)))
    start = time.time()

    for i in rand_arr:
        i += 1
    print('np array: ' + str(time.time() - start))


array()
numpy_array()

# zad 2



rand_arr = np.random.random(10000)
start = time.time()
for i in rand_arr:
    numpy.sin(i) + numpy.cos(i)
print('np array: ' + str(time.time() - start))

start = time.time()
print(numpy.sin(rand_arr) + numpy.cos(rand_arr))
print('np array: ' + str(time.time() - start))


# zad 3
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


def cube_sum_num(x):
    """Zwraca sume szescianow elementow"""
    result = 0
    for i in range(len(x)):
        result += numpy.power(x[i], 3)
    return result


def almost_variance_num(x):
    """Oblicza 1/n * SUM (x_i - mean(x))^4"""
    m = numpy.divide(sum(x), len(x))
    result = 0
    for i in range(len(x)):
        result += numpy.power((x[i] - m), 4)
    result = numpy.divide(result, len(x))
    return result


# zad 5

array = np.array([[]])
for i in range(10):
    array = numpy.append(array, [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)], axis=2)
print('array: '+str(array))