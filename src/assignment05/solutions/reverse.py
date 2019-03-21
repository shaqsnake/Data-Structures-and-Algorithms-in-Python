class Node:
    def __init__(self, e):
        self._element = e
        self._next = None

    def __repr__(self):
        res = "HEAD->"
        while self:
            res += str(self._element) + '->'
            self = self._next
        res += 'None'
        return res


def reverse_list(head):
    """
    :type head: Node
    :rtype: Node
    """
    if not head and not head._next:
        return head
    prev = None
    while head:
        current = head
        head = head._next
        current._next = prev
        prev = current
    return prev


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1._next = n2
    n2._next = n3
    n3._next = n4
    print(n1)
    n = reverse_list(n1)
    print(n)