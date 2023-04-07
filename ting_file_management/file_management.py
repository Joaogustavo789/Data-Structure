import sys


def txt_importer(path_file):
    # print(path_file)

    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido")

    # list_text = list(path_file)
    # return list_text
