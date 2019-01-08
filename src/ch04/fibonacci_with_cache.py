from utils.clockdeco import clock


def cache(func):
    mem = {}

    def func_wrapper(n):
        if n not in mem.keys():
            mem[n] = func(n)
        return mem[n]

    return func_wrapper


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
