def log(func):
    def inner(*args, **kwargs):
        print(func.__name__, f'args: {args}')
        return func(*args)
    return inner

@log
def soma(x, y):
    return x + y
