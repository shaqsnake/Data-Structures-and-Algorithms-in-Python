from abc import ABC, abstractmethod


class AbstractDeque(ABC):

    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    @abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @abstractmethod
    def add_first(self, e):
        raise NotImplementedError

    @abstractmethod
    def add_last(self, e):
        raise NotImplementedError

    @abstractmethod
    def del_first(self):
        raise NotImplementedError

    @abstractmethod
    def del_last(self):
        raise NotImplementedError

    @abstractmethod
    def first(self):
        raise NotImplementedError

    @abstractmethod
    def last(self):
        raise NotImplementedError

