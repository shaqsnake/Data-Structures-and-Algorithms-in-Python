class DoubleLinkedList:
    class _Node:
        __slots__ = ('_element', '_prev', '_next')

        def __init__(self, e):
            self._element = e
            self._prev = None
            self._next = None

    def __init__(self):
        """Create a empty double linked list.
        """
        self._header = self._Node(None)
        self._tailer = self._Node(None)
        self._header._next = self._tailer
        self._tailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        p = self._header._next
        while p is not self._tailer:
            yield p._element
            p = p._next

    def __repr__(self):
        res = ' <-> '.join(map(str, self))
        return 'header <-> ' + res + ' <-> tailer'

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add a node betweent two existing nodes.
        """
        node = self._Node(e)
        node._prev = predecessor
        node._next = successor
        predecessor._next = node
        successor._prev = node
        self._size += 1
        return node

    def _remove_node(self, node):
        """Remove node from the double linked list.
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        res = node._element
        node._prev = node._next = node._element = None
        return res
