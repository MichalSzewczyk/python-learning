# Generators - allows to reuse results of previous calls
# generators returns an iterator that generates a stream of values
# in functions each call generates new namespace and local variable
# in generators everything is accessible

def gen_example(n):
    prev = 0
    actual = 0
    for i in range(n):
        prev = actual
        actual = i
        yield prev + actual


print(max(gen_example(100)))
