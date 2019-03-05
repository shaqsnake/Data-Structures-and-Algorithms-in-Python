from random import shuffle


def findRightFirstLargeNum(l):
    """
    :type l: List[int]
    :rtype: List[int]
    """
    res = [-1] * len(l)
    stack = []

    for i in range(len(l)):
        while len(stack) > 0 and l[stack[-1]] < l[i]:
            res[stack.pop()] = i
        stack.append(i)   
    return res


if __name__ == '__main__':
    l = [i for i in range(10)]
    shuffle(l)
    print(l)
    print(findRightFirstLargeNum(l))
