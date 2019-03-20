import random
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


if __name__ == "__main__":
    l = list(range(1, 10))
    random.shuffle(l)
    bubble_sort(l, True)
    random.shuffle(l)
    insertion_sort(l, True)
    random.shuffle(l)
    selection_sort(l, True)
    random.shuffle(l)
    print(merge_sort(l))
    random.shuffle(l)
    quick_sort(l, True)