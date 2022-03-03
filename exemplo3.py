def tag_html(func):
    # func é uma variável livre

    def interna(*args, **kwargs):
        return f'<html>{func(*args, **kwargs)}</html>'
        print('depois de executar a funcao')

    return interna

@tag_html
def ola_bb():
    return 'Dentro da função'


@tag_html
def live():
    return 'Live de python'