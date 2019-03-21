class Node:
    def __init__(self, e):
        self._element = e
        self._next = None


def is_cyclic(head):
    """
    :type head: Node
    :rtype: bool
    """
    if not head:
        return False

    runner = walker = head
    while runner._next and runner._next._next:
        runner = runner._next._next
        walker = walker._next
        if runner == walker:
            return True

    return False


if __name__ == "__main__":
    ll = Node('a')
    n1 = Node('b')
    n2 = Node('c')
    n3 = Node('d')
    n4 = Node('e')
    n5 = Node('f')
    n6 = Node('g')
    ll._next = n1
    n1._next = n2
    n2._next = n3
    n3._next = n4
    n4._next = n5
    n5._next = n6
    print(is_cyclic(ll))

    n6._next = n3
    print(is_cyclic(ll))