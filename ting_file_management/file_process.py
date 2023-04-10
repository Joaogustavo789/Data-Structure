import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    # print(path_file)
    # print(instance)
    for repeat_file in range(len(instance)):
        if path_file in instance.search(repeat_file).values():
            return None

    process_file = txt_importer(path_file)

    # print(process_file)
    line_count = len(process_file)

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": line_count,
        "linhas_do_arquivo": process_file
    }

    # print(new_dict)

    instance.enqueue(new_dict)
    sys.stdout.write(str(new_dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
