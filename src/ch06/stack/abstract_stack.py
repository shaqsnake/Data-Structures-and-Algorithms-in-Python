from abc import ABC, abstractmethod


class AbstractStack(ABC):
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
        raise NotImplementedError

    @abstractmethod
    def push(self, e):
        raise NotImplementedError

    @abstractmethod
    def pop(self):
        raise NotImplementedError

    @abstractmethod
    def peek(self):
        raise NotImplementedError
