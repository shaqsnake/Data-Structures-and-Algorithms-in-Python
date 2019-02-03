import pytest
from circular_queue2 import CircularQueue


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
    it = iter(circular_queue)
    for i in range(9):
        assert next(it) == i

    for i in range(8):
        assert circular_queue.dequeue() == i
    assert circular_queue.peek() == 8

    circular_queue.enqueue('a')
    circular_queue.enqueue('b')

    assert circular_queue.dequeue() == 8
    assert circular_queue.dequeue() == 'a'
    assert circular_queue.dequeue() == 'b'


def test_circular_queue_could_resize_automatically(circular_queue):
    for i in range(10):
        circular_queue.enqueue(i)
    assert len(circular_queue) == 10
    assert len(circular_queue._array) == 10

    circular_queue.enqueue(10)
    assert len(circular_queue) == 11
    assert len(circular_queue._array) == 20

    for _ in range(7):
        circular_queue.dequeue()

    assert len(circular_queue) == 4
    assert len(circular_queue._array) == 10
