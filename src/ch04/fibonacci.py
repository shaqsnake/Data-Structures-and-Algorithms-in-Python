from functools import lru_cache
from utils.clockdeco import clock


@lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    print(fibonacci(5))