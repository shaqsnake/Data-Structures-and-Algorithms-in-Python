# Merge k sorted linked lists and return it as one sorted list.
# The time complexity should be O(nlogn)
# Input: [ 1->4->5, 1->3->4, 2->6 ]
# Output: 1->1->2->3->4->4->5->6
from heapq import heapify, heappop, heapreplace

class ListNode:
    def __init__(self, v):
        self.v = v
        self.next = None

    def __lt__(self, other):
        return self.v < other.v

def build_lists(tow_dim_list):
    res = []
    for l in tow_dim_list:
        dummy = node = ListNode(0)
        while l:
            n = ListNode(l.pop(0))
            node.next = n
            node = node.next
        res.append(dummy.next)
    return res

def iter_list(node):
    res = []
    while node:
        res.append(node.v)
        node = node.next
    return res


def merge_sorted_lists(lists):
    dummy = node = ListNode(0)
    heap = [(n.v, n) for n in lists if n]
    heapify(heap)
    while heap:
        _, n = heap[0]
        if n.next is None:
            heappop(heap)
        else:
            heapreplace(heap, (n.next.v, n.next))
        node.next = n
        node = node.next
    return dummy.next

if __name__ == "__main__":
    data = build_lists([[1, 4, 5], [1, 3, 4], [2, 6]])
    print(iter_list(merge_sorted_lists(data)))