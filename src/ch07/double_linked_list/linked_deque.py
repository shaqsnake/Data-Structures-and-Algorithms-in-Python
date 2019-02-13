from double_linked_list import DoubleLinkedList


class LinkedDeque(DoubleLinkedList):
    def first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._tailer._prev._element

    def add_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        self._insert_between(e, self._tailer._prev, self._tailer)

    def del_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._remove_node(self._header._next)

    def del_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._remove_node(self._tailer._prev)


if __name__ == "__main__":
    deque = LinkedDeque()
    for i in range(5):
        deque.add_first(i)

    for x in 'abcde':
        deque.add_last(x)

    print(deque)

    print(deque.del_first())
    print(deque.del_first())
    print(deque.del_first())
    print(deque.del_last())
    print(deque.del_last())
    print(deque.del_last())
    print(deque)
