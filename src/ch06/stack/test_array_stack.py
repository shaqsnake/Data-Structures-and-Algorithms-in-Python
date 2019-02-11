import pytest
from array_stack import ArrayStack


@pytest.fixture()
def stack():
    s = ArrayStack()
    s.push(1)
    s.push(['a', 'b'])
    s.push(('t1', 't2'))
    return s


def test_array_stack_features(stack):
    assert stack.is_empty() is False
    assert len(stack) == 3
    assert stack.peek() == ('t1', 't2')
    assert stack.pop() == ('t1', 't2')
    assert len(stack) == 2
    assert stack.peek() == ['a', 'b']
    stack.pop()
    stack.pop()
    assert len(stack) == 0
    assert stack.is_empty() is True

    with pytest.raises(IndexError):
        stack.pop()


def test_array_stack_iter(stack):
    for i in range(1, 10):
        stack.push(i)

    it = iter(stack)
    for i in range(9, 0, -1):
        assert next(it) == i
