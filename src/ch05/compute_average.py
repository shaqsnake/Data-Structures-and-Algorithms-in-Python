from utils.clockdeco import clock


@clock
def compute_average(n):
    data = []
    for _ in range(n):
        data.append(None)


if __name__ == "__main__":
    for k in (10**exp for exp in range(2, 8)):
        compute_average(k)