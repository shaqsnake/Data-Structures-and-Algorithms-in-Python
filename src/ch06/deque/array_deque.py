from abstract_deque import AbstractDeque


class ArrayDeque(AbstractDeque):
    def __init__(self, data=None):
        super().__init__()
        if data is None:
            self._array = []
        else:
            self._array = list(data)
        self._size = len(self._array)

    def __iter__(self):
        return (x for x in self._array)

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


if __name__ == "__main__":
    deque1 = ArrayDeque([1, 2, 3])
    deque1.add_first(0)
    deque1.add_last(4)
    print(deque1._array)

    deque2 = ArrayDeque()
    deque2.add_first('a')
    deque2.add_last('b')
    print(deque2._array)

    deque3 = ArrayDeque()
    print(deque3._array)

    deque3.add_first('what')
    deque3.add_last('TF')
    print(deque1._array)
    print(deque2._array)
    print(deque3._array)

    print(deque1._array is deque2._array)
    print(deque3._array is deque2._array)
