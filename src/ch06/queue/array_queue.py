from abstract_queue import AbstractQueue


class ArrayQueue(AbstractQueue):
    def __init__(self, cap=10):
        super().__init__()
        self._array = [None] * cap
        self._front = 0
        self._rear = 0

    def __iter__(self):
        p = self._front
        while p <= self._rear:
            yield self._array[p]
            p += 1

    def enqueue(self, e):
        if self._rear == len(self._array):
            self._expand()
        self._array[self._rear] = e
        self._rear += 1
        self._size += 1

    def _expand(self):
        """expands cap of the array.
        Time Complexity: O(n).
        """
        self._array += [None] * len(self._array)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        res = self._array[self._front]
        self._array[self._front] = None
        self._front += 1
        self._size -= 1
        return res

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._array[self._front]
