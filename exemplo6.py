'''Decorador com params'''
from functools import wraps

def validate_type(type):
    # type é liver
    def _validate(func):
        # func é liver
        @wraps(func)
        def inner(*args, **kwargs):
            if all(isinstance(val, type) for val in args):
                return func(*args)
            else:
                print('deu ruim')
        return inner
    return _validate

@validate_type(int)
def soma_inteiro(x, y):
    return x + y