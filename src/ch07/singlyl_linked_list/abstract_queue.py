from abc import ABC, abstractmethod


class AbstractQueue(ABC):

    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        return "->".join(map(str, self))

    def is_empty(self):
        return self._size == 0

    @abstractmethod
    def enqueue(self, e):
        raise NotImplementedError

    @abstractmethod
    def dequeue(self):
        raise NotImplementedError

    @abstractmethod
    def peek(self):
        raise NotImplementedError

    @abstractmethod
    def __iter__(self):
        raise NotImplementedError
