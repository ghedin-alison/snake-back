def valida_inteiro(func):
    def interna(*args):
        if all(isinstance(val, int) for val in args):
            return func(*args)
        else:
            return 'Deu ruim!'
    return interna

@valida_inteiro
def soma(*args):
    return sum(args)
