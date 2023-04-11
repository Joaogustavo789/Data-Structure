def exists_word(word, instance):
    print(instance)

    for find_word in range(len(instance)):
        if word not in instance.search(find_word).values():
            return []

    new_list = [
        {
            "palavra": word,
            "arquivo": "statics/nome_pedro.txt",
            "ocorrencias": [
                {
                    "linha": ""
                },

                {
                    "linha": ""
                }
            ]
        }
    ]

    return new_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
