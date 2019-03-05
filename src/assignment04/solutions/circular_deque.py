class CircularDeque:
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self._data = [None for _ in range(k)]
        self._front = 0
        self._rear = 1
        self._size = 0

    def __len__(self):
        return self._size

    def _move(self, curr, steps):
        curr = (curr + steps + len(self._data)) % len(self._data)
        return curr

    def add_first(self, e):
        """
        Adds an item at the front of Deque.
        Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            raise IndexError("Deque is full")
        self._data[self._front] = e
        # self._front = (self._front - 1) % len(self._data)
        self._front = self._move(self._front, -1)
        self._size += 1

    def add_last(self, e):
        """
        Adds an item at the rear of Deque.
        Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            raise IndexError("Deque is full")
        self._data[self._rear] = e
        self._rear = self._move(self._rear, 1)
        self._size += 1

    def del_first(self):
        """
        Deletes an item from the front of Deque.
        Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            raise IndexError("Deque is empty")
        # self._front = (self._front + 1) % len(self._data)
        self._front = self._move(self._front, 1)
        res = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        return res

    def del_last(self):
        """
        Deletes an item from the rear of Deque.
        Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            raise IndexError("Deque is empty")
        self._rear = self._move(self._rear, -1)
        res = self._data[self._rear]
        self._data[self._rear] = None
        self._size -= 1
        return res

    def first(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            raise IndexError("Deque is empty")
        idx = self._move(self._front, 1)
        return self._data[idx]

    def last(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            raise IndexError("Deque is empty")
        idx = self._move(self._rear, -1)
        return self._data[idx]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        # Make sure you add self.size to check if start and end diff is 1
        return self._size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self._front == self._rear


if __name__ == "__main__":
    deque = CircularDeque(5)
    print(deque._data)

    deque.add_first(3)
    deque.add_last(5)
    print(deque._data)

    deque.add_first(7)
    print(deque._data)

    print(deque.del_first())
    print(deque.del_first())

    deque.add_last('a')
    deque.add_last('b')
    print(deque._data)

    print(deque.del_first())

    deque.add_last('c')
    deque.add_last('d')
    print(deque._data)
    print(deque.first())
    print(deque.last())
