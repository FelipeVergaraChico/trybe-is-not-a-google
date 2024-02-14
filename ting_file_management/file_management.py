import sys


def txt_importer(path_file):
    if '.txt' not in path_file:
        sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file, 'r') as file:
            c = file.read()
            res = c.split('\n')
            file.close()
            return res
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
