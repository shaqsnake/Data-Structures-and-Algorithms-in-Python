import pytest
from array_queue import ArrayQueue


@pytest.fixture
def array_queue():
    return ArrayQueue()


def test_array_queue_constructor():
    aq1 = ArrayQueue()
    assert len(aq1._array) == 10

    aq2 = ArrayQueue(20)
    assert len(aq2._array) == 20


def test_array_queue_enqueue_and_dequeue(array_queue):
    for i in range(10):
        array_queue.enqueue(i)

    assert len(array_queue) == 10
    it = iter(array_queue)
    for i in range(10):
        assert next(it) == i

    for i in range(10):
        assert array_queue.dequeue() == i


def test_array_queue_expand_automatically(array_queue):
    for i in range(10):
        array_queue.enqueue(i)

    assert len(array_queue._array) == 10
    array_queue.enqueue('a')
    assert len(array_queue._array) == 20


def test_array_queue_peek(array_queue):
    array_queue.enqueue(0)
    assert array_queue.peek() == 0

    array_queue.enqueue(1)
    assert array_queue.peek() == 0
