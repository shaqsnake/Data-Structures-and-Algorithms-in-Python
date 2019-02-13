from abstract_stack import AbstractStack
from node import SinglyLinkedListNode


class LinkedListStack(AbstractStack):

    def __init__(self):
        super().__init__()
        self._head = None

    def __iter__(self):
        p = self._head
        while p is not None:
            yield p._element
            p = p._next

    def push(self, e):
        node = SinglyLinkedListNode(e)
        node._next = self._head
        self._head = node
        self._top += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        res = self._head._element
        self._head = self._head._next
        self._top -= 1
        return res

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._head._element


if __name__ == "__main__":
    stack = LinkedListStack()
    for i in range(5):
        stack.push(i)
    print(stack)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack)
