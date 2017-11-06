# passing functions as arguments to another functions:
import timeit


def func(fn, *args, **kwargs):
    fn(*args, **kwargs)


# and invocation:
func(lambda x: print(x), 10)


# it is also possible to return function from the function:
def func_outer(x):
    def func_inner(y):
        print(str(x) + str(y))

    return func_inner


# and invocation:
func_outer('first and ')('second')


# Decorators - use both approaches
def decorator(fn):
    def decorator_method(*args, **kwargs):
        print('Invocation of method: ' + str(fn))
        result = fn(*args, **kwargs)
        print('Method executed.')
        return result

    return decorator_method


@decorator
def method(arg):
    print('executing method with arg: {}!'.format(arg))


method('foo')


def decorator(func):
    def decorating(*args, **kwargs):
        print('decorating!')
        return func(*args, **kwargs)

    return decorating


@decorator
def decorated():
    print('Hello!')


decorated()


# decorators are extremely useful when it comes to perform some instrumentation:
def time_measure_decorator(fn):
    def decorate(*args, **kwargs):
        timer = timeit.Timer(lambda: fn(*args, **kwargs))
        execution_time = timer.timeit()
        print(execution_time)

    return decorate


@time_measure_decorator
def slow_method(n):
    for i in range(n):
        for j in range(i):
            ignore = j ** i


slow_method(2)


# It is also possible to define decorators with arguments. Example:
def parametrized_decorator(x):
    def internal_decorator(fn):
        def decorating_function(*args, **kwargs):
            print('Decorator parameter: {}'.format(x))
            result = fn(*args, **kwargs)
            print('Method {} executed.'.format(fn.__name__))
            return result

        return decorating_function

    return internal_decorator


@parametrized_decorator('foo')
def method():
    print('Executing method.')


method()
