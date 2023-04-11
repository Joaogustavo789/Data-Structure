from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue_priority = PriorityQueue()

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue_priority.search(3)

    new_dict = {
        "nome_do_arquivo": "arquivo.txt",
        "qtd_linhas": 9,
        "linhas_do_arquivo": None
    }

    new_dict2 = {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": None
    }

    new_dict3 = {
        "nome_do_arquivo": "arquivo3.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": None
    }

    queue_priority.enqueue(new_dict)
    queue_priority.enqueue(new_dict2)
    queue_priority.enqueue(new_dict3)

    length1 = queue_priority.__len__()

    assert length1 == 3

    queue_priority.dequeue()

    length2 = queue_priority.__len__()

    assert length2 == 2

    find_index = queue_priority.search(0)

    assert find_index == new_dict3

# [9, 4, 2]
# [4, 2, 9]
# [9, 2]
# [2, 9]
