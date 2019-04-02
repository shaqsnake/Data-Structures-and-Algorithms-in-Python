def is_isomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    tmp_dict = dict()
    tmp_set = set()
    for i in range(len(s)):
        if s[i] not in tmp_dict:
            if t[i] in tmp_set:
                return False
            tmp_dict[s[i]] = t[i]
            tmp_set.add(t[i])
        else:
            if tmp_dict[s[i]] != t[i]:
                return False
    return True


if __name__ == "__main__":
    print(is_isomorphic("add", "tee"))
    print(is_isomorphic("mom", "man"))
    print(is_isomorphic("paper", "title"))
    print(is_isomorphic("foo", "bar"))
    print(is_isomorphic("gaga", "coco"))
    print(is_isomorphic("abc", "bbc"))
