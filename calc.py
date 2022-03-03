from argparse import ArgumentParser

parser = ArgumentParser(prog='calculadora',
                        description='''
                        Calculadora via linha de comando''',
                        fromfile_prefix_chars='@')

parser.add_argument('operacao',
                    type=str,
                    help='Como vc gostaria de usar a calculadora?')
parser.add_argument('x',
                    type=int,
                    help='Primeiro valor')
parser.add_argument('y',
                    type=int,
                    help='Segundo valor')
parser.add_argument('-v', '--verbose',
                    action='count',
                    help='Entenda o que estamos fazendo', default=0)

args = parser.parse_args()

def verbose(func):
    def _inner(x, y):
        if args.verbose == 1:
            print(f'Estamos operando com {x} e {y}')
        elif args.verbose == 2:
            print(f'{func.__name__} ({x} e {y})')
        elif args.verbose >= 10:
            print(f'Vá se danar com tanta verbosidade')
            exit()
        return func(x, y)
    return _inner

@verbose
def soma(x, y):
    return x + y

@verbose
def sub(x, y):
    return x - y

@verbose
def multiplica(x, y):
    return x * y

@verbose
def divide(x, y):
    return x / y

if __name__ == '__main__':
    operacoes = {'soma': soma,
                 'sub': sub,
                 'multiplica': multiplica,
                 'divide': divide}
    print(operacoes[args.operacao](args.x, args.y))