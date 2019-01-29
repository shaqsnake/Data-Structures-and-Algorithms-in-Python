from functools import lru_cache


@lru_cache()
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    return climbStairs(n - 1) + climbStairs(n - 2)


if __name__ == "__main__":
    print(climbStairs(10))
