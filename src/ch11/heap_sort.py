def heapify(arr, n, i):
    largest = i
    lchild = 2 * i
    rchild = 2 * i + 1

    if lchild < n and arr[i] < arr[
            lchild]:  # exist left child and left child is larger
        largest = lchild

    if rchild < n and arr[largest] < arr[
            rchild]:  # exist right child and right child is larger
        largest = rchild

    if largest != i:  # left child or right child is larger
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def buildHeap(arr):
    for i in range(len(l) // 2, 0, -1):  # from last non-leaf node to the root
        heapify(l, len(l), i)


def heapSort(arr):
    buildHeap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(arr, i, 1)


if __name__ == "__main__":
    l = [(0)]
    l.extend([7, 3, 19, 9, 4, 1, 20, 11, 15])
    print(l[1:])

    buildHeap(l)
    print(l[1:])

    heapSort(l)
    print(l[1:])