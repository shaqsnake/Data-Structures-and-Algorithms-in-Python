from utils.clockdeco import clock


@clock
def fib_tail_recur(n, res, temp):
    if n == 0:
        return res
    return fib_tail_recur(n - 1, temp, res + temp)


if __name__ == "__main__":
    print(fib_tail_recur(5, 0, 1))
