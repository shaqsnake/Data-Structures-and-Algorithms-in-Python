class CircularQueue:
    def __init__(self, cap=10):
        self._array = [None] * cap
        self._front = 0
        self._rear = 0

    def __len__(self):
        if self._rear >= self._front:
            return self._rear - self._front
        return len(self._array) - (self._front - self._rear)

    def enqueue(self, e):
        if len(self) == len(self._array) - 1:
            raise IndexError("Queue is full")
        self._array[self._rear] = e
        self._rear = (self._rear + 1) % len(self._array)

    def dequeue(self):
        if len(self) == 0:
            raise IndexError("Queue is empty")
        res = self._array[self._front]
        self._array[self._front] = None
        self._front = (self._front + 1) % len(self._array)
        return res


if __name__ == "__main__":
    queue = CircularQueue()
    for i in range(9):
        queue.enqueue(i)

    queue.dequeue()
    queue.enqueue('a')
    queue.dequeue()
    queue.enqueue('b')

    print(queue._array)
