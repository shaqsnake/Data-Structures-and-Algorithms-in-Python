from utils.clockdeco import clock


def cache(func):
    mem = {}
    hit = 0

    def wrapper(n):
        nonlocal hit
        if n not in mem.keys():
            mem[n] = func(n)
        else:
            hit += 1
            print("cache hit @%s(%d)" % (func.__name__, n))
        return mem[n]

    return wrapper


@cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    print(fibonacci(5))
    print(fibonacci(6))
    print(fibonacci(8))
