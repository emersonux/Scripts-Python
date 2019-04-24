#!/usr/bin/python3

import yaml
import json
import sys
import errno


def conversao(arquivo):
    # Tratativa de erro do arquivo origem não existir
    try:
        with open(arquivo, encoding='utf-8') as entrada:
            dados_json = json.load(entrada)
    except FileNotFoundError as error:
        print(error)
        help()
        sys.exit(errno.ENOENT)
    else:
        return yaml.dump(dados_json, default_flow_style=False)


def help():
    print('É necessário digitar o local do arquivo json \
e opcionalmente o arquivo de saída\n')
    print(
        f'Sintaxe: {sys.argv[0][2:]} </path/arquivo.json> [<saida> opcional]')


if __name__ == '__main__':
    # Verifica se os argumentos foram passados de forma correta
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        help()
        sys.exit(errno.EPERM)
    else:
        '''Executa pegando o arquivo de entrada,caso seja informado a mesma
        será gravada no segundo argumento.'''
        arquivo = sys.argv[1]
        resultado = conversao(arquivo)
        if len(sys.argv) == 3:
            saida = sys.argv[2]
            sys.stdout = open(f'{saida}.yaml', 'w')
            print(resultado)
        else:
            print(resultado)
