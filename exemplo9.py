from functools import partial


def soma(x, y):
    return x + y

soma_2 = partial(soma, 2)
soma_3 = partial(soma, 3)