from ting_file_management.priority_queue import PriorityQueue
import pytest


mock_queue_high_priority = {
        'nome_do_arquivo': 'arquivo_teste.txt',
        'qtd_linhas': 3,
        'linhas_do_arquivo': [...]
    }

mock_queue_regular_priority = {
        'nome_do_arquivo': 'arquivo_grande.txt',
        'qtd_linhas': 6,
        'linhas_do_arquivo': [...]
    }


def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue(mock_queue_regular_priority)
    assert len(queue) == 1
    queue.enqueue(mock_queue_high_priority)
    assert len(queue) == 2
    assert queue.search(0) == mock_queue_high_priority
    with pytest.raises(IndexError):
        queue.search(99) == mock_queue_regular_priority
    queue.dequeue()
    queue.dequeue()
    assert len(queue) == 0
