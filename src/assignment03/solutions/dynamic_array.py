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
        if not 0 <= k < self._len:
            raise IndexError("wrong index")
        return self._A[k]

    def append(self, val):
        """Add element to the end of array.
        """
        if self._len == self._cap:
            self._expand()
        self._A[self._len] = val
        self._len += 1

    def _expand(self):
        """Expand double capacity when the size of array
        is lower than 1000, else expand only 1.25x.
        """
        if self._cap < 1000:
            self._resize(2 * self._cap)
        else:
            self._resize(self._cap + self._cap // 4)

    def _resize(self, cap):
        B = self._make_array(cap)
        for i in range(self._len):
            B[i] = self._A[i]
        self._A = B
        self._cap = cap

    def insert(self, k, val):
        """Insert value at index k and shifting subsequent values rightward.
        """
        if self._len == self._cap:
            self._expand()
        # shifting the sub array to right
        for i in range(self._len, k, -1):
            self._A[i] = self._A[i - 1]
        self._A[k] = val
        self._len += 1

    def remove(self, val):
        """Remove first occurrence of value, raise Value Error if not match.
        """
        for k in range(self._len):
            if self._A[k] == val:
                for i in range(k, self._len - 1):
                    self._A[i] = self._A[i + 1]
                self._A[self._len - 1] = None
                self._len -= 1
                if 0 <= self._len <= self._cap // 4:
                    self._cap //= 2
                return
        raise ValueError('value not found')

    def pop(self):
        """Remove last element and return its value, raise Value Error if not match.
        """
        if self._len == 0:
            raise IndexError("empty array")
        res = self._A[self._len - 1]
        self._A[self._len - 1] = None
        self._len -= 1
        if 0 <= self._len <= self._cap // 4:
            self._cap //= 2
        return res
