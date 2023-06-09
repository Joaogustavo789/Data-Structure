import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido")

    try:
        with open(path_file) as file_txt:
            lines = file_txt.read()
            list_txt = lines.split("\n")

            return list_txt

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
