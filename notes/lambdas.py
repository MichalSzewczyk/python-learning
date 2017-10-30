list = ['foo', 'bar', 'foobar']

for i in map(lambda x: 'Processing {}.'.format(x), list):
    print(i)
