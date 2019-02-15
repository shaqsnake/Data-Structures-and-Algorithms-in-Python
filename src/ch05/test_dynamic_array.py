import pytest

from dynamic_array import DynamicArray


def test_dynamic_array_should_get_element_by_its_index():
    da = DynamicArray()
    for i in range(10):
        da.append(i)
        assert da[i] == i


def test_dynamic_array_should_double_capacity_automatically():
    da = DynamicArray()
    for i in range(2):
        da.append(i)
    assert len(da) == 2
    assert da[0] == 0
    assert da[1] == 1

    da.append(2)
    assert da._cap == 4


def test_dynamic_array_should_raises_IndexError_when_it_is_out_of_index():
    da = DynamicArray()
    with pytest.raises(IndexError, match="wrong index"):
        da[1]


def test_dynamic_array_should_return_specified_value_after_insert():
    da = DynamicArray()
    da.insert(0, 1)
    assert da[0] == 1
    assert len(da) == 1
    assert da._cap == 1

    da.insert(0, 2)
    assert len(da) == 2
    assert da._cap == 2
    assert da[0] == 2

    da.insert(2, 3)
    assert len(da) == 3
    assert da._cap == 4
    assert da[2] == 3


def test_dynamic_array_should_remove_specified_element():
    da = DynamicArray()
    da.append(1)
    da.append(2)
    da.append(3)
    da.remove(2)
    assert da[0] == 1
    assert da[1] == 3

    da.remove(1)
    assert da[0] == 3
    