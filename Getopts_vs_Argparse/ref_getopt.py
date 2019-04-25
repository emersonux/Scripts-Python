#!/usr/bin/python3

import sys
import getopt
import errno

primeiro_argumento = None
segundo_argumento = None

comando_completo = sys.argv[1:]
# print(comando_completo)
try:
    opts, args = getopt.getopt(
        # O caractere : e = após a opção significa que a mesma
        # exige um argumento
        comando_completo, "p:s:h", [
            'primeiro-argumento=', 'segundo-argumento=', 'help'
        ]
    )

except getopt.GetoptError as error:
    print(error)
    sys.exit(errno.EPERM)

for opt, arg in opts:
    if opt in ['-p', '--primeiro-argumento']:
        primeiro_argumento = arg
        print(f'primeiro argumento: {primeiro_argumento}')
    elif opt in ['-s', '--segundo-argumento']:
        segundo_argumento = arg
        print(f'segundo_argumento: {segundo_argumento}')
    elif opt in ['-h', '--help']:
        print('help com sucesso')
