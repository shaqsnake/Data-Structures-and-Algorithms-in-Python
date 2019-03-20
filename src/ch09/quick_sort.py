def quick_sort(data, sim=False):
    iteration = 0
    if sim:
        print("== Quick Sort ===")
        print("iteration", iteration, ":", *data)
    data, _ = quick_sort_recur(data, 0, len(data) - 1, iteration, sim)
    return data


def quick_sort_recur(data, first, last, iteration, sim):
    if first < last:
        pos = partition(data, first, last)
        if sim:
            iteration += 1
            print("iteration", iteration, ":", *data)

        _, iteration = quick_sort_recur(data, first, pos - 1, iteration, sim)
        _, iteration = quick_sort_recur(data, pos + 1, last, iteration, sim)

    return data, iteration


def partition(data, first, last):
    pos = first
    for cur in range(first, last):
        if data[cur] < data[last]:  # last is the pivot
            data[cur], data[pos] = data[pos], data[cur]
            pos += 1
    data[pos], data[last] = data[last], data[pos]
    return pos
