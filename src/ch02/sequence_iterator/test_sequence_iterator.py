import pytest
from sequence_iterator import SequenceIterator


def test_sequence_iterator_constructor():
    data = [x for x in range(10)]
    si = SequenceIterator(data)

    assert isinstance(si, SequenceIterator) == True
    assert si._seq == data
    assert si._k == -1


def test_sequence_iterator_next():
    data = [x for x in range(3)]
    si = SequenceIterator(data)

    assert next(si) == 0
    assert next(si) == 1
    assert next(si) == 2

    with pytest.raises(StopIteration):
        next(si)


def test_sequece_iterator_iter():
    si = SequenceIterator([1, 2, 3])
    assert si is iter(si)