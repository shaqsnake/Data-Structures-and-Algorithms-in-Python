# Reverse a binary tree, like below：
# Input:
#                 4
#              /      \
#            2         7
#           / \       /   \
#         1     3    6     9
# Output:
#                 4
#              /      \
#            7         2
#           / \       /   \
#         9     6    3     1


class TreeNode:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None


def list_to_binarytree(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    node.left = list_to_binarytree(nums[:mid])
    node.right = list_to_binarytree(nums[mid + 1:])
    return node


def inorder_traversal(node):
    if node:
        yield from inorder_traversal(node.left)
        yield node.v
        yield from inorder_traversal(node.right)


def reverse_tree(node):
    if node is None:
        return
    node.left, node.right = node.right, node.left
    if node.left:
        reverse_tree(node.left)
    if node.right:
        reverse_tree(node.right)


if __name__ == "__main__":
    binary_tree = list_to_binarytree([1, 2, 3, 4, 6, 7, 9])
    print([n for n in inorder_traversal(binary_tree)])
    reverse_tree(binary_tree)
    print([n for n in inorder_traversal(binary_tree)])

    l = [x for x in range(10)]
    binary_tree = list_to_binarytree(l)
    print([n for n in inorder_traversal(binary_tree)])
    reverse_tree(binary_tree)
    print([n for n in inorder_traversal(binary_tree)])

    from random import shuffle
    shuffle(l)
    binary_tree = list_to_binarytree(l)
    print([n for n in inorder_traversal(binary_tree)])
    reverse_tree(binary_tree)
    print([n for n in inorder_traversal(binary_tree)])
