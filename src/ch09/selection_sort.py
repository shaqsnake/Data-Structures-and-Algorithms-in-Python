def selection_sort(data, sim=False):
    iteration = 0
    if sim:
        print("=== Selection Sort ===")
        print("iteration", iteration, ":", *data)

    for i in range(len(data)):
        minPos = i

        for j in range(i + 1, len(data)):
            if data[j] < data[minPos]:
                minPos = j

        data[minPos], data[i] = data[i], data[minPos]

        if sim:
            iteration += 1
            print("iteration", iteration, ":", *data)

    return data