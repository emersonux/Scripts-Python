#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description='Exemplo de opções e Argumentos')
parser.add_argument('-r', '--run', action='store_true',
                    help='Rodar o Programa sem argumentos')
parser.add_argument(
    '-p', '--primeiro-arg-composto', type=str, help='Primeiro Argumento'
)
parser.add_argument(
    '-s', '--segundo-argumento', type=str, help='Segundo Argumento'
)

args = parser.parse_args()

# Chamada da função da opção run.
if args.run:
    print("função teste com sucesso")

print(
    f'primiro argumento: {args.primeiro_arg_composto}\n\
segundo argumento: {args.segundo_argumento}'
)
