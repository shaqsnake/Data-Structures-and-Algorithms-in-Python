class TreeNode:
    def __init__(self, data):
        self._data = data
        self._children = []

    def __repr__(self, level=0):
        res = "\t" * level + repr(self._data) + "\n"
        for child in self._children:
            res += child.__repr__(level + 1)
        return res


class BSTNode:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def __iter__(self):
        if self._left:
            yield from self._left
        yield self._data
        if self._right:
            yield from self._right


if __name__ == "__main__":
    a = TreeNode('A')
    b = TreeNode('B')
    c = TreeNode('C')
    d = TreeNode('D')
    e = TreeNode('E')
    f = TreeNode('F')
    g = TreeNode('G')
    h = TreeNode('H')
    i = TreeNode('I')
    j = TreeNode('J')
    a._children.append(b)
    a._children.append(c)
    a._children.append(d)
    b._children.extend([e, f])
    d._children.extend([g, h])
    h._children.extend([i, j])
    print(a)