from abc import ABCMeta, abstractmethod


class AbstractStack(metaclass=ABCMeta):
    """Abstract Class for Stacks."""
    def __init__(self):
        self._top = -1

    def __len__(self):
        return self._top + 1

    def __repr__(self):
        res = "->".join(map(str, self))
        return 'Top->' + res

    def is_empty(self):
        return self._top == -1

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def push(self, e):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass
