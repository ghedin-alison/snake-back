from argparse import ArgumentParser

parser = ArgumentParser(prog='test',
                        usage='test[arg]',
                        description='Mensagem do help',
                        epilog='Entendeu??',
                        fromfile_prefix_chars='@')
# parser.add_argument('x') # argumento obrigatório
parser.add_argument('-foo', '-f', '--foo') # argumento opcional [-]

parser.add_argument('-bar', '-b', '--bar', action='append_const', const=str, dest='xpto') # store é padrão para action

parser.add_argument('-add', '-a', '--add', action='append', dest='xpto') # action=append pra adicionar numa lista

parser.add_argument('-v', action='count') # action=count
parser.add_argument('-c', choices=[1, 2, 3],
                    default=0,
                    type=int,
                    help='Opcões [1, 2, 3]') # action=count


parser.print_help()
args = parser.parse_args()

print(args)
