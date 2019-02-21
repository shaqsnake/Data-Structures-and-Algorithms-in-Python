import random
from binary_search_tree import BinarySearchTree


def test_bst_size():
    bst = BinarySearchTree()
    assert len(bst) == 0

    for i in range(5):
        bst.insert(i)
        assert len(bst) == i + 1


def test_bst_insert_at_right_pos():
    bst = BinarySearchTree()
    bst.insert(15)
    assert bst._root._data == 15

    bst.insert(12)
    assert bst._root._left._data == 12

    bst.insert(18)
    assert bst._root._right._data == 18

    bst.insert(16)
    assert bst._root._right._left._data == 16

    assert repr(bst) == "12 15 16 18"

    bst2 = BinarySearchTree()
    data = [x for x in range(10)]
    random.shuffle(data)
    for i in data:
        bst2.insert(i)
    assert repr(bst2) == ' '.join(map(str, sorted(data)))


def test_bst_search():
    bst = BinarySearchTree([5, 1, 6, 3, 8])
    assert bst.search(1) == True
    assert bst.search(10) == False
    assert bst.search(8) == True

    bst.insert(100)
    assert bst.search(100) == True
