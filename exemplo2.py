def decorador(func):
    # func é uma variável livre

    def interna(*args, **kwargs):
        print('antes de executar a funcao')
        func(*args, **kwargs)
        print('depois de executar a funcao')

    return interna

@decorador
def ola_bb():
    print('Dentro da função')