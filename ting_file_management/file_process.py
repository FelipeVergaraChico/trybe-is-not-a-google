import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index) == path_file:
            return
    instance.enqueue(path_file)
    data = txt_importer(path_file)
    dict = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data
    }
    print(dict)


def remove(instance):
    if len(instance) == 0:
        print('Não há elementos')
        return
    f_queue = instance.dequeue()
    print(f'Arquivo {f_queue} removido com sucesso')


def file_metadata(instance, position):
    try:
        path = instance.search(position)
        N_instance = Queue()
        process(path, N_instance)
    except IndexError:
        sys.stderr.write('Posição inválida')
