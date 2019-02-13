from abstract_queue import AbstractQueue
from node import SinglyLinkedListNode


class LinkedListQueue(AbstractQueue):

    def __init__(self):
        super().__init__()
        self._head = None
        self._tail = None

    def __iter__(self):
        p = self._head
        while p is not None:
            yield p._element
            p = p._next

    def enqueue(self, e):
        node = SinglyLinkedListNode(e)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
            self._tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        res = self._head._element
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head._next
        self._size -= 1
        return res

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._head._element


if __name__ == "__main__":
    queue = LinkedListQueue()
    for i in range(5):
        queue.enqueue(i)
    print(queue)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue)
