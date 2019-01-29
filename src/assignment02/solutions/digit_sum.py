def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


if __name__ == "__main__":
    print(digit_sum(10302))
