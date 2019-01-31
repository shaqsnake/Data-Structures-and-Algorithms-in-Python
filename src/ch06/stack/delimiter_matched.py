from array_stack import ArrayStack


def delimiter_matched_v1(expr):
    """Return True if all delimiters are properly match; False otherwise.

    >>> delimiter_matched_v1('[(2+x)*(3+y)]')
    True

    >>> delimiter_matched_v1('{[{(xbcd))]}')
    False
    """
    left, right = '({[', ')}]'
    S = ArrayStack()

    for c in expr:
        if c in left:
            S.push(c)
        elif c in right:
            if S.is_empty() or right.index(c) != left.index(S.pop()):
                return False
    return S.is_empty()


def delimiter_matched_v2(expr: str) -> bool:
    """
    >>> delimiter_matched_v2('[(2+x)*(3+y)]')
    True

    >>> delimiter_matched_v2('{[{(xbcd))]}')
    False
    """
    S = ArrayStack()
    d = {")": "(", "]": "[", "}": "{"}

    for c in expr:
        if c in d.values():
            S.push(c)
        elif c in d:
            if S.is_empty() or d[c] != S.pop():
                return False
    return S.is_empty()


if __name__ == "__main__":
    import doctest
    doctest.testmod()