import random


def counting_sort(data):
    k = max(data)
    temp = [0] * (k + 1)  # arr contain the number i appear counts in data

    for i in range(len(data)):
        temp[data[i]] = temp[data[i]] + 1

    for i in range(1, k + 1):
        temp[i] = temp[i - 1] + temp[i]

    sorted_data = data.copy()
    # for i in range(len(data) - 1, -1, -1):
    for i in range(len(data)):
        sorted_data[temp[data[i]] - 1] = data[i]
        temp[data[i]] -= 1

    return sorted_data


if __name__ == "__main__":
    data = [random.randrange(0, 10, 1) for _ in range(100)]
    print(data)
    print(counting_sort(data))
