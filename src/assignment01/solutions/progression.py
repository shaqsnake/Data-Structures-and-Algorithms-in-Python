class Progression:
    """Iterator producting a generic progression.

    Default iterator produces the whole numbers 0, 1, 2...
    """

    def __init__(self, start=0):
        """Initilize current value to the first value of the progression.
        """
        self._cur_val = start

    def _advance(self):
        """Update sefl._cur_val to a new value.

        This should be overriden by a subclass to customize progression.
        """
        self._cur_val += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error.
        """
        if self._cur_val is None:
            raise StopIteration()
        res = self._cur_val
        self._advance()
        return res

    def __iter__(self):
        """Return itself as an iterator.
        """
        return self

    def print_progression(self, n):
        """Print next n values of the progression.
        """
        print(' '.join(str(next(self)) for _ in range(n)))


class ArithmeticProgression(Progression):
    def __init__(self, inc=1, start=0):
        super().__init__(start)
        self._inc = inc

    def _advance(self):
        self._cur_val += self._inc


class GeometricProgression(Progression):
    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._cur_val *= self._base


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._cur_val = self._cur_val, self._prev + self._cur_val


if __name__ == "__main__":
    p = Progression()
    p.print_progression(10)
    ap = ArithmeticProgression(2)
    ap.print_progression(10)
    gp = GeometricProgression()
    gp.print_progression(10)
    fp = FibonacciProgression()
    fp.print_progression(10)
