def exists_word(word, instance):
    # print(instance.showQueue())

    new_list = []

    for file in instance.showQueue():
        ocorrencias = []

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                ocorrencias.append(
                    {
                        "linha": index + 1
                    },
                )

        if ocorrencias:
            exist_word_list = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": ocorrencias
            }

            new_list.append(exist_word_list)

    return new_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
