def validate_int(func):
    # func é uma variável livre

    def validate(*args):
        print(list(args))
        return func(*args)

    return validate

def soma(*args):
    return sum(args)

soma_com_validacao = validate_int(soma)