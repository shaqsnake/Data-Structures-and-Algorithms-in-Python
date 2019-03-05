def validateStackSequences(pushed, popped):
    """
    :type pushed: List[int]
    :type popped: List[int]
    :rtype: bool
    """
    stack = []
    for v in pushed:
        stack.append(v)
        while len(stack) > 0 and popped[0] == stack[-1]:
            stack.pop()
            popped.pop(0)

    return len(stack) == 0


if __name__ == "__main__":
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    print(validateStackSequences(pushed, popped))

    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    print(validateStackSequences(pushed, popped))