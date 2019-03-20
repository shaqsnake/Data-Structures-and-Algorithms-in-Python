def insertion_sort(data, sim=False):
    iteration = 0
    if sim:
        print("== Insertion Sort ===")
        print("iteration", iteration, ":", *data)

    for i in range(len(data)):
        cur = data[i]
        pos = i

        while pos > 0 and data[pos - 1] > cur:
            data[pos] = data[pos - 1]
            pos = pos - 1
        data[pos] = cur

        if sim:
            iteration += 1
            print("iteration", iteration, ":", *data)

    return data
