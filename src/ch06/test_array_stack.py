import pytest
from array_stack import ArrayStack, Empty


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
    assert stack.top() == ('t1', 't2')
    assert stack.pop() == ('t1', 't2')
    assert len(stack) == 2
    assert stack.top() == ['a', 'b']
    stack.pop()
    stack.pop()
    assert len(stack) == 0
    assert stack.is_empty() is True

    with pytest.raises(Empty):
        stack.pop()
