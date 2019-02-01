import pytest
from circle_queue import CircleQueue


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

    for i in range(8):
        assert circle_queue.dequeue() == i

    circle_queue.enqueue('a')
    circle_queue.enqueue('b')
    assert circle_queue.dequeue() == 8
    assert circle_queue.dequeue() == 'a'
    assert circle_queue.dequeue() == 'b'
