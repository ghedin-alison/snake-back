def validate_type(type, *args):
    return all(isinstance(val, type) for val in args)


def soma(x, y):
    '''
    :param x: primeiro valor
    :param y: segundo valor
    :return: resultado da soma de dois valores
    '''
    if all(isinstance(val, int) for val in [x, y]):
        return x + y


def sub(x, y):
    '''
    :param x: primeiro valor
    :param y: segundo valor
    :return: resultado da subtração de dois valores
    '''
    if all(isinstance(val, int) for val in [x, y]):
        return x - y
