from treenode import BSTNode as Node


class AvlTree(object):
    """
    An avl tree.
    """

    def __init__(self):
        # Root node of the tree.
        self.node = None
        self.height = -1
        self.balance = 0

    def insert(self, data):
        """
        Insert new data into node
        """
        # Create new node
        n = Node(data)
        if not self.node:
            self.node = n
            self.node._left = AvlTree()
            self.node._right = AvlTree()
        elif data < self.node._data:
            self.node._left.insert(data)
        elif data > self.node._data:
            self.node._right.insert(data)
        self.re_balance()

    def re_balance(self):
        """
        Re balance tree. After inserting or deleting a node,
        """
        self.update_heights(recursive=False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node._left.balance < 0:
                    self.node._left.rotate_left()
                    self.update_heights()
                    self.update_balances()
                self.rotate_right()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node._right.balance > 0:
                    self.node._right.rotate_right()
                    self.update_heights()
                    self.update_balances()
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        """
        Update tree height
        """
        if self.node:
            if recursive:
                if self.node._left:
                    self.node._left.update_heights()
                if self.node._right:
                    self.node._right.update_heights()

            self.height = 1 + max(self.node._left.height,
                                  self.node._right.height)
        else:
            self.height = -1

    def update_balances(self, recursive=True):
        """
        Calculate tree balance factor
        """
        if self.node:
            if recursive:
                if self.node._left:
                    self.node._left.update_balances()
                if self.node._right:
                    self.node._right.update_balances()

            self.balance = self.node._left.height - self.node._right.height
        else:
            self.balance = 0

    def rotate_right(self):
        """
        Right rotation
        """
        new_root = self.node._left.node
        new_left_sub = new_root._right.node
        old_root = self.node

        self.node = new_root
        old_root._left.node = new_left_sub
        new_root._right.node = old_root

    def rotate_left(self):
        """
        Left rotation
        """
        new_root = self.node._right.node
        new_left_sub = new_root._left.node
        old_root = self.node

        self.node = new_root
        old_root._right.node = new_left_sub
        new_root._left.node = old_root

    def in_order_traverse(self):
        """
        In-order traversal of the tree
        """
        result = []

        if not self.node:
            return result

        result.extend(self.node._left.in_order_traverse())
        result.append(self.node._data)
        result.extend(self.node._right.in_order_traverse())
        return result

    def pre_order_traverse(self):
        """
        Pre-order traversal of the tree
        """
        result = []

        if not self.node:
            return result

        result.append(self.node._data)
        result.extend(self.node._left.in_order_traverse())
        result.extend(self.node._right.in_order_traverse())
        return result


if __name__ == "__main__":
    avl = AvlTree()
    for i in range(10):
        avl.insert(i)

    print(avl.in_order_traverse())
    print(avl.pre_order_traverse())
