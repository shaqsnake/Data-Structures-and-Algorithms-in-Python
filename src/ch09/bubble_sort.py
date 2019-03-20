def bubble_sort(data, sim=False):
    def swap(i, j):
        data[i], data[j] = data[j], data[i]

    iteration = 0
    if sim:
        print("== Bubble Sort ===")
        print("iteration", iteration, ":", *data)

    swapped = True
    p = -1
    while swapped:
        swapped = False
        p += 1
        for i in range(1, len(data) - p):
            if data[i - 1] > data[i]:
                swap(i - 1, i)
                swapped = True
                if sim:
                    iteration += 1
                    print("iteration", iteration, ":", *data)

    return data
