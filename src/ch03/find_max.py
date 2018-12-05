def find_max(data):
    """Return the maximum element from a nonempty Python list.
    """
    max = data[0]
    for val in data:
        if val > max:
            max = val
    return max