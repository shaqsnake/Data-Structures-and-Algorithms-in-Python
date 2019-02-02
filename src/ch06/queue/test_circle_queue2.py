import pytest
from circle_queue2 import CircleQueue


@pytest.fixture
def circle_queue():
    return CircleQueue()


def test_circle_queue_constructor():
    queue = CircleQueue()
    assert len(queue) == 0
    assert len(queue._array) == 10


def test_circle_queue_features(circle_queue):
    for i in range(9):
        circle_queue.enqueue(i)

    assert len(circle_queue) == 9
    it = iter(circle_queue)
    for i in range(9):
        assert next(it) == i

    for i in range(8):
        assert circle_queue.dequeue() == i
    assert circle_queue.peek() == 8

    circle_queue.enqueue('a')
    circle_queue.enqueue('b')

    assert circle_queue.dequeue() == 8
    assert circle_queue.dequeue() == 'a'
    assert circle_queue.dequeue() == 'b'


def test_circle_queue_could_resize_automatically(circle_queue):
    for i in range(10):
        circle_queue.enqueue(i)
    assert len(circle_queue) == 10
    assert len(circle_queue._array) == 10

    circle_queue.enqueue(10)
    assert len(circle_queue) == 11
    assert len(circle_queue._array) == 20

    for _ in range(7):
        circle_queue.dequeue()

    assert len(circle_queue) == 4
    assert len(circle_queue._array) == 10
