from utils.clockdeco import clock


@clock
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    factorial(6)
