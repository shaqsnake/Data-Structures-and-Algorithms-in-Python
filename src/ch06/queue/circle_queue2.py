from abstract_queue import AbstractQueue


class CircleQueue(AbstractQueue):
    """Circle Queue implementation using a Python list as underlying storage.
    """
    def __init__(self, cap=10):
        super().__init__()
        self._array = [None] * cap
        self._front = 0

    def __iter__(self):
        p = self._front
        while p != (self._front + self._size) % len(self._array):
            yield self._array[p]
            p = (p + 1) % len(self._array)

    def enqueue(self, e):
        if self._size == len(self._array):
            self._resize(2 * len(self._array))
        rear = (self._front + self._size) % len(self._array)
        self._array[rear] = e
        self._size += 1

    def _resize(self, cap):
        tmp = self._array
        self._array = [None] * cap
        p = self._front
        for i in range(self._size):
            self._array[i] = tmp[p]
            p = (p + 1) % len(tmp)
        self._front = 0

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        res = self._array[self._front]
        self._array[self._front] = None
        self._front = (self._front + 1) % len(self._array)
        self._size -= 1
        if 0 < self._size < len(self._array) // 4:
            self._resize(len(self._array) // 2)
        return res

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._array[self._front]


if __name__ == "__main__":
    queue = CircleQueue()
    for i in range(10):
        queue.enqueue(i)
    print(queue._array)

    queue.dequeue()
    queue.enqueue('a')
    queue.dequeue()
    queue.enqueue('b')
    print(queue._array)

    queue.enqueue('c')
    print(queue._array)
