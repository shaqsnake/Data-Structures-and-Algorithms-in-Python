import pytest
from circular_queue import CircularQueue


@pytest.fixture
def circular_queue():
    return CircularQueue()


def test_circular_queue_constructor():
    queue = CircularQueue()
    assert len(queue) == 0
    assert len(queue._array) == 10


def test_circular_queue_features(circular_queue):
    for i in range(9):
        circular_queue.enqueue(i)

    assert len(circular_queue) == 9

    for i in range(8):
        assert circular_queue.dequeue() == i

    circular_queue.enqueue('a')
    circular_queue.enqueue('b')
    assert circular_queue.dequeue() == 8
    assert circular_queue.dequeue() == 'a'
    assert circular_queue.dequeue() == 'b'
