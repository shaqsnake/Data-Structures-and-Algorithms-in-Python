from binary_search import binary_search

def test_binary_search():
    d = [1, 2, 5, 6, 7, 9, 10, 13, 16, 17, 21, 24, 27, 33]
    assert binary_search(d, 2, 0, len(d)) == 1
    assert binary_search(d, 24, 0, len(d)) == 11
    assert binary_search(d, 3, 0, len(d)) == -1
    assert binary_search(d, 0, 0, len(d)) == -1
    assert binary_search(d, 34, 0, len(d)) == -1