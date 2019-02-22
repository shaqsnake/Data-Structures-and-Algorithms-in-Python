def preorder(node):
    if node:
        yield node._data
        yield from preorder(node._left)
        yield from preorder(node._right)


def inorder(node):
    if node:
        yield from inorder(node._left)
        yield node._data
        yield from inorder(node._right)


def postorder(node):
    if node:
        yield from postorder(node._left)
        yield from postorder(node._right)
        yield node._data


if __name__ == "__main__":
    import random
    from binary_search_tree import BinarySearchTree

    data = [x for x in range(20)]
    random.shuffle(data)
    bst = BinarySearchTree(data)

    bst.get_root().display()
    print([i for i in preorder(bst.get_root())])
    print([i for i in inorder(bst.get_root())])
    print([i for i in postorder(bst.get_root())])