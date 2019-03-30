from abc import ABC, abstractmethod


class AbstractHeap(ABC):
    """Abstract class for binary heap.
    """

    def __init__(self):
        pass

    @abstractmethod
    def siftUp(self, i):
        pass

    @abstractmethod
    def siftDown(self, i):
        pass

    @abstractmethod
    def insert(self, v):
        pass

    @abstractmethod
    def removeMax(self):
        pass


class Heap(AbstractHeap):
    def __init__(self):
        self._size = 0
        self._array = [(0)]

    def __repr__(self):
        return ' '.join(map(str, self._array[1:]))

    def insert(self, v):
        self._array.append(v)
        self._size += 1
        self.siftUp(self._size)

    def siftUp(self, i):
        while i // 2 > 0:
            if self._array[i] > self._array[i // 2]:
                self._array[i], self._array[i // 2] = self._array[
                    i // 2], self._array[i]
            i //= 2

    def removeMax(self):
        res = self._array[1]
        self._array[1] = self._array[self._size]
        self._size -= 1
        self._array.pop()
        self.siftDown(1)
        return res

    def siftDown(self, i):
        while 2 * i < self._size:
            max_child = self.maxChild(i)
            if self._array[i] < self._array[max_child]:
                self._array[i], self._array[max_child] = self._array[
                    max_child], self._array[i]
            i = max_child

    def maxChild(self, i):
        if 2 * i + 1 > self._size:  # no right child
            return 2 * i
        else:
            # left child > right child
            if self._array[2 * i] > self._array[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1


if __name__ == "__main__":
    heap = Heap()
    heap.insert(33)
    heap.insert(17)
    heap.insert(21)
    heap.insert(11)
    heap.insert(13)
    heap.insert(15)
    heap.insert(9)
    heap.insert(1)
    heap.insert(2)
    heap.insert(7)
    heap.insert(12)
    heap.insert(10)
    print(heap)
    heap.insert(24)
    print(heap)
    heap.removeMax()
    print(heap)
