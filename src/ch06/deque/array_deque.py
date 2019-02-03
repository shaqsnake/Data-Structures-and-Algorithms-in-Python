from abstract_deque import AbstractDeque


class ArrayDeque(AbstractDeque):
    def __init__(self, data=[]):
        super().__init__()
        self._array = data
        self._size = len(data)

    def add_first(self, e):
        self._array.insert(0, e)
        self._size += 1

    def add_last(self, e):
        self._array.append(e)
        self._size += 1

    def del_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        self._array.pop(0)
        self._size -= 1

    def del_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        self._array.pop()
        self._size -= 1

    def first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._array[0]

    def last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._array[-1]
