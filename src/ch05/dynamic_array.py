import ctypes


class DynamicArray:
    """A simplified Python list which provides low-level array.
    """

    def __init__(self):
        """Create an empty array when initialied.
        """
        self._len = 0
        self._cap = 1
        self._A = self._make_array(self._cap)

    def _make_array(self, cap):
        """Return new array with capacity.
        """
        return (cap * ctypes.py_object)()

    def __len__(self):
        """Return the number of elements in array.
        """
        return self._len

    def __getitem__(self, k):
        """Return the element of array which indexed at k.
        """
        if not 0 <= k <= self._len:
            raise IndexError("wrong index")
        return self._A[k]

    def append(self, element):
        """Add element to the end of array.
        """
        if self._len == self._cap:
            self._resize(2 * self._cap)
        self._A[self._len] = element
        self._len += 1

    def _resize(self, cap):
        B = self._make_array(cap)
        for i in range(self._len):
            B[i] = self._A[i]
        self._A = B
        self._cap = cap

