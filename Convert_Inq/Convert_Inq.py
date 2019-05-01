#!/usr/bin/python3

import argparse
import sys

cabecalho = ['Device', 'Vendor',
             'Product', 'Revision', 'Serial Number', 'Size KB']


def argumentos():
    parser = argparse.ArgumentParser(
        description='Conversor da saida do inq para CSV'
    )
    parser.add_argument('-i', '--input-file', required=True, type=str,
                        metavar='</path/input_file>',
                        help='REQUIRED - Inform INQ text file')

    parser.add_argument('-o', '--output-file', type=str,
                        metavar='<output.csv>',
                        help='OPTIONAL - default output on stdout')

    args = parser.parse_args()

    if len(sys.argv) == 3:
        na_tela(args.input_file)
    else:
        no_arquivo(args.input_file, args.output_file)


def na_tela(file):
    with open(file) as entrada:
        dados = entrada.read()
        print(', '.join(cabecalho))
        for linha in dados.splitlines():
            tratado = linha.strip().split(':')
            # print(f'{tratado[0]},{tratado[1]},{tratado[2]}...)
            print(','.join(tratado))


def no_arquivo(file_in, file_out):
    with open(file_in) as entrada:
        dados = entrada.read()
        with open(file_out, 'w') as saida:
            print(', '.join(cabecalho), file=saida)
            for linha in dados.splitlines():
                tratado = linha.strip().split(':')
                print(','.join(tratado), file=saida)


if __name__ == '__main__':
    argumentos()
