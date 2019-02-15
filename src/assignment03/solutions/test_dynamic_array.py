import pytest

from dynamic_array import DynamicArray


@pytest.fixture()
def dynamic_array():
    da = DynamicArray()
    return da


def test_dynamic_array_should_get_element_by_its_index(dynamic_array):
    for i in range(10):
        dynamic_array.append(i)
        assert dynamic_array[i] == i


def test_dynamic_array_should_expand_automatically(dynamic_array):
    import math
    for i in range(1000):
        dynamic_array.append(i)
        assert i < dynamic_array._cap
        if i == 0:
            assert dynamic_array._cap == 1
        else:
            assert dynamic_array._cap == pow(2, math.floor(math.log2(i) + 1))

    for i in range(1000, 1025):
        dynamic_array.insert(0, i)
    assert dynamic_array._cap == 1024 + 1024 // 4


def test_dynamic_array_should_raises_IndexError_when_it_is_out_of_index(
        dynamic_array):
    with pytest.raises(IndexError, match="wrong index"):
        dynamic_array[1]


def test_dynamic_array_should_store_value_after_insert_or_append(
        dynamic_array):
    for i in range(10):
        dynamic_array.append(i)
        assert dynamic_array[i] == i

    for i in range(10):
        dynamic_array.insert(0, i)
        assert dynamic_array[0] == i


def test_dynamic_array_should_remove_specified_element(dynamic_array):
    dynamic_array.append(1)
    dynamic_array.append(2)
    dynamic_array.append(3)
    dynamic_array.remove(2)
    assert dynamic_array[0] == 1
    assert dynamic_array[1] == 3

    dynamic_array.remove(1)
    assert dynamic_array[0] == 3


def test_dynamic_array_should_pop_element(dynamic_array):
    for i in range(10):
        dynamic_array.append(i)

    for i in range(9, 0, -1):
        assert i == dynamic_array.pop()


def test_dynamic_array_should_shrink_automatically(dynamic_array):
    for i in range(64):
        dynamic_array.append(i)
    assert len(dynamic_array) == 64
    assert dynamic_array._cap == 64

    for i in range(48):
        dynamic_array.pop()
    assert len(dynamic_array) == 16
    assert dynamic_array._cap == 32

    for i in range(8):
        dynamic_array.pop()
    assert len(dynamic_array) == 8
    assert dynamic_array._cap == 16

    for i in range(4):
        dynamic_array.pop()
    assert len(dynamic_array) == 4
    assert dynamic_array._cap == 8

    for i in range(2):
        dynamic_array.pop()
    assert len(dynamic_array) == 2
    assert dynamic_array._cap == 4

    dynamic_array.remove(0)
    assert len(dynamic_array) == 1
    assert dynamic_array._cap == 2

    dynamic_array.remove(1)
    assert len(dynamic_array) == 0
    assert dynamic_array._cap == 1
