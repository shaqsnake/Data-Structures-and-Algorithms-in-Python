from abstract_stack import AbstractStack


class ArrayStack(AbstractStack):
    """LIFO Stack implementation using a Python list as underlying storage.
    """

    def __init__(self):
        """Create an empty stack."""
        super().__init__()
        self._data = []

    def __iter__(self):
        p = self._top
        while p >= 0:
            yield self._data[p]
            p -= 1

    def push(self, e):
        """Add element e to the top of stack."""
        self._top += 1
        self._data.append(e)

    def pop(self):
        """Remove and return the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        self._top -= 1
        return self._data.pop()

    def peek(self):
        """Return (not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[self._top]
