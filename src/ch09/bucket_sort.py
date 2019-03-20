import random


def bucket_sort(data):

    bucket_num = len(data)
    buckets = [[] for _ in range(bucket_num)]

    for v in data:
        index = v * bucket_num // (max(data) + 1)
        buckets[index].append(v)

    sorted_data = []
    for i in range(bucket_num):
        sorted_data.extend(sorted(buckets[i]))
    return sorted_data


if __name__ == "__main__":
    data = [random.randrange(1, 10000, 1) for _ in range(100)]
    print(data)
    print(bucket_sort(data))
