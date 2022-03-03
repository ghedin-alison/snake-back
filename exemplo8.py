from functools import singledispatch

@singledispatch
def gerar_html(x):
    return x

@gerar_html.register(int)
def _gerar_com_int(x):
    return f'<span>{x}</span>'

@gerar_html.register(list)
def _gerar_com_list(x):
    return f'<p>{x}</p>'

@gerar_html.register(str)
def _gerar_com_str(x):
    return f'<h1>{x}</h1>'
