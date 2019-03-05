import pytest
from circular_deque import CircularDeque


def test_circular_deque_should_add_and_remove_element_at_the_front():
    deque = CircularDeque(5)
    assert len(deque) == 0
    assert deque._data == [None, None, None, None, None]
    assert deque._front == 0
    assert deque._rear == 1

    deque.add_first(3)
    assert len(deque) == 1
    assert deque._data == [3, None, None, None, None]
    assert deque._front == 4
    assert deque._rear == 1

    deque.add_first(5)
    assert len(deque) == 2
    assert deque._data == [3, None, None, None, 5]
    assert deque._front == 3
    assert deque._rear == 1

    deque.add_first(7)
    deque.add_first(9)
    assert len(deque) == 4
    assert deque._data == [3, None, 9, 7, 5]
    assert deque._front == 1
    assert deque._rear == 1

    with pytest.raises(IndexError, match="Deque is full"):
        deque.add_first(11)

    assert deque.del_first() == 9
    assert deque.del_first() == 7
    assert deque.del_first() == 5
    assert len(deque) == 1
    assert deque.del_first() == 3

    with pytest.raises(IndexError, match="Deque is empty"):
        deque.del_first()


def test_circular_deque_should_add_and_remove_element_at_the_rear():
    deque = CircularDeque(5)
    assert len(deque) == 0
    assert deque._data == [None, None, None, None, None]
    assert deque._front == 0
    assert deque._rear == 1

    deque.add_last(2)
    assert len(deque) == 1
    assert deque._data == [None, 2, None, None, None]
    assert deque._front == 0
    assert deque._rear == 2

    deque.add_last(4)
    deque.add_last(6)
    deque.add_last(8)
    assert len(deque) == 4
    assert deque._data == [None, 2, 4, 6, 8]
    assert deque._front == 0
    assert deque._rear == 0

    with pytest.raises(IndexError, match="Deque is full"):
        deque.add_last(10)

    assert deque.del_last() == 8
    assert deque.del_last() == 6
    assert deque.del_last() == 4
    assert deque.del_last() == 2

    with pytest.raises(IndexError, match="Deque is empty"):
        deque.del_last()


def test_circular_deque_should_return_first_or_last_element():
    deque = CircularDeque(5)
    deque.add_first(1)
    assert deque.first() == 1

    deque.add_last('a')
    assert deque.last() == 'a'
