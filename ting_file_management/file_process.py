import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for repeat_file in range(len(instance)):
        if path_file in instance.search(repeat_file).values():
            return None

    process_file = txt_importer(path_file)

    line_count = len(process_file)

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": line_count,
        "linhas_do_arquivo": process_file
    }

    instance.enqueue(new_dict)

    sys.stdout.write(str(new_dict))


def remove(instance):
    if instance.__len__() == 0:
        sys.stdout.write("Não há elementos\n")

    else:
        path_file = instance.dequeue()

        file_path = path_file['nome_do_arquivo']

        sys.stdout.write(f"Arquivo {file_path} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)

        sys.stdout.write(str(file))

    except IndexError:
        sys.stderr.write("Posição inválida")
