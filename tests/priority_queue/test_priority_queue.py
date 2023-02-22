from ting_file_management.priority_queue import PriorityQueue
import pytest

def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue({"qtd_linhas": 1})
    queue.enqueue({"qtd_linhas": 12})
    queue.enqueue({"qtd_linhas": 9})

    assert len(queue) == 3
    assert len(queue.regular_priority) == 2
    assert len(queue.high_priority) == 1

    queue.dequeue() == {"qtd_linhas": 12}

    assert len(queue) == 2
    assert len(queue.regular_priority) == 2
    assert len(queue.high_priority) == 0

    assert queue.search(0) == {"qtd_linhas": 12}
    assert queue.search(1) == {"qtd_linhas": 9}

    with pytest.raises(IndexError):
        queue.search(99)