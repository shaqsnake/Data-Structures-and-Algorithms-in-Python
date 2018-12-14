import pytest

from dynamic_array import DynamicArray


def test_dynamic_array_get_element_by_index():
    da = DynamicArray()
    for i in range(10):
        da.append(i)
        assert da[i] == i

def test_dynamic_array_double_capacity_automatically():
    da = DynamicArray()
    for i in range(2):
        da.append(i)
    assert len(da) == 2
    assert da[0] == 0
    assert da[1] == 1

    da.append(2)
    assert da._cap == 4

def test_dynamic_array_should_raises_IndexError_when_out_of_index():
    da = DynamicArray()
    with pytest.raises(IndexError, match="wrong index"):
        da[1]