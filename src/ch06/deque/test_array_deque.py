from array_deque import ArrayDeque


def test_circle_deque_features():
    deque = ArrayDeque()
    assert len(deque) == 0
    assert deque.is_empty() == True

    deque.add_last(5)
    assert deque._array == [5]

    deque.add_first(3)
    assert deque._array == [3, 5]

    deque.add_first(7)
    assert deque._array == [7, 3, 5]

    assert deque.first() == 7

    deque.del_last()
    assert len(deque) == 2
    assert deque._array == [7, 3]

    deque.del_first()
    assert deque._array == [3]
    assert deque.is_empty() == False

    deque2 = ArrayDeque([1, 2, 3])
    assert deque2._array == [1, 2, 3]