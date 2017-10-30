def decorator(func):
    def decorating():
        print('decorating!')
        return func()

    return decorating


@decorator
def decorated():
    print('Hello!')

decorated()
