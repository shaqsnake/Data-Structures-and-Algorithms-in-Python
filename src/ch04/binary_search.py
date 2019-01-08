from utils.clockdeco import clock


@clock
def binary_search(data, target, low, high):
    """Return position if target is found in indicated portion of a python list and -1 if target is not found.
    """
    if low > high:
        return -1

    mid = (low + high) // 2
    if target == data[mid]:
        return mid
    elif target < data[mid]:
        # recur on the portion left of the middle
        return binary_search(data, target, low, mid - 1)
    else:
        # recur on the portion right of the middle
        return binary_search(data, target, mid + 1, high)


if __name__ == "__main__":
    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    binary_search(data, 23, 0, len(data) - 1)
