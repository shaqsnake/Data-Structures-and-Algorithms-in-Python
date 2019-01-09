class Empty(Exception):
    """Error attempting to access an element from an empty container.
    """
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage.
    """

    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def __len__(self):
        """Return the # of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return Ture if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of stack."""
        self._data.append(e)

    def pop(self):
        """Remove and return the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def top(self):
        """Return (not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]
