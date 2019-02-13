from abstract_queue import AbstractQueue
from node import SinglyLinkedListNode


class CircularQueue(AbstractQueue):
    def __init__(self):
        super().__init__()
        self._tail = None

    def __iter__(self):
        p = self._tail._next
        while True:
            yield p._element
            if p is self._tail:
                return
            p = p._next

    def enqueue(self, e):
        node = SinglyLinkedListNode(e)
        if self.is_empty():
            node._next = node
        else:
            node._next = self._tail._next
            self._tail._next = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        remove_node = self._tail._next
        if len(self) == 1:
            self._tail = None
        else:
            self._tail._next = remove_node._next
        self._size -= 1
        return remove_node._element

    def peek(self):
        return self._tail._next._element

    def rotate(self):
        if len(self) > 0:
            self._tail = self._tail._next


if __name__ == "__main__":
    queue = CircularQueue()
    for i in range(5):
        queue.enqueue(i)
    print(queue)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue)
    queue.rotate()
    print(queue)