import random


def radix_sort(data, simulation=False):
    position = 1
    max_number = max(data)

    iteration = 0
    if simulation:
        print("=== Radix Sort ===")
        print("iteration", iteration, ":", *data)

    while position < max_number:
        queue_list = [list() for _ in range(10)]

        for num in data:
            digit_number = num // position % 10
            queue_list[digit_number].append(num)

        index = 0
        for numbers in queue_list:
            for num in numbers:
                data[index] = num
                index += 1

        if simulation:
            iteration = iteration + 1
            print("iteration", iteration, ":", *data)

        position *= 10
    return data


if __name__ == "__main__":
    data = [random.randrange(10**4, 10**5, 1) for _ in range(10)]
    radix_sort(data, True)