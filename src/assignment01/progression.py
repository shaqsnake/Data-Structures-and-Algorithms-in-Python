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
        # TODO: Implement this method.
        pass

    def __iter__(self):
        """Return itself as an iterator.
        """
        # TODO: Implement this method.
        pass

    def print_progression(self, n):
        """Print next n values of the progression.
        """
        # TODO: Implement this method.
        pass
