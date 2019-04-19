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


def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1


if __name__ == "__main__":
    binary_tree = list_to_binarytree([x for x in range(10)])
    print(height(binary_tree))