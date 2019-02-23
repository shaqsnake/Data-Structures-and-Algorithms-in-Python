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

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self._right is None and self._left is None:
            line = '%s' % self._data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self._right is None:
            lines, n, p, x = self._left._display_aux()
            s = '%s' % self._data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self._left is None:
            lines, n, p, x = self._right._display_aux()
            s = '%s' % self._data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._left._display_aux()
        right, m, q, y = self._right._display_aux()
        s = '%s' % self._data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


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