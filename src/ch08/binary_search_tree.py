from treenode import BSTNode as Node


class BinarySearchTree:
    def __init__(self, iterable=None):
        self._root = None
        if iterable:
            for v in iterable:
                self.insert(v)

    def __len__(self):
        return self._size(self._root)

    def __repr__(self):
        return ' '.join(map(str, self.get_root()))

    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node._left) + self._size(node._right)

    def get_root(self):
        return self._root

    def insert(self, data):
        if self._root is None:
            self._root = Node(data)
        else:
            self._recur_insert(self._root, data)

    def _recur_insert(self, node, data):
        if data == node._data:
            return
        elif data < node._data:
            if node._left:
                self._recur_insert(node._left, data)
            else:
                node._left = Node(data)
        else:
            if node._right:
                self._recur_insert(node._right, data)
            else:
                node._right = Node(data)

    def search(self, data):
        return self._recur_search(self._root, data)

    def _recur_search(self, node, data):
        if node is None:
            return False
        if data == node._data:
            return True
        elif data < node._data:
            return self._recur_search(node._left, data)
        else:
            return self._recur_search(node._right, data)

    def delete(self, data):
        node = self.get_root()
        parent = None
        # 遍历定位到待删除节点和其父节点
        while node and node._data != data:
            parent = node
            if data < node._data:
                node = node._left
            else:
                node = node._right
        if node is None:
            return

        # 如果待删除节点有左右子树
        if node._left and node._right:
            rightMinNode = node._right
            rightMinNodeParent = node
            while rightMinNode._left:
                rightMinNodeParent = rightMinNode
                rightMinNode = rightMinNode._left
            node._data = rightMinNode._data
            node = rightMinNode
            parent = rightMinNodeParent

        # 待删除节点只有一个子节点或者没有子节点
        child = None
        if node._left is not None:
            child = node._left
        elif node._right is not None:
            child = node._right

        if parent is None:  # 如果删除跟节点
            self._root = child
        elif parent._left == node:
            parent._left = child
        else:
            parent._right = child


if __name__ == "__main__":
    bst = BinarySearchTree([5, 1, 6, 3, 8])
    bst.get_root().display()
