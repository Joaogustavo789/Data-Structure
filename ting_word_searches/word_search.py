def exists_word(word, instance):
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
    new_list2 = []

    for file2 in instance.showQueue():
        ocorrencias2 = []

        for index2, line2 in enumerate(file2["linhas_do_arquivo"]):
            if word.lower() in line2.lower():
                ocorrencias2.append(
                    {
                        "linha": index2 + 1,
                        "conteudo": line2
                    },
                )

        if ocorrencias2:
            exist_word_list2 = {
                "palavra": word,
                "arquivo": file2["nome_do_arquivo"],
                "ocorrencias": ocorrencias2
            }

            new_list2.append(exist_word_list2)

    return new_list2
