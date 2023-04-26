from math import log10, floor, sqrt


def ans(n: int) -> list:
    limit = 10 ** 6
    if (n == 1):
        return [-1]

    a = n - 1
    b = 1
    c = 1

    if a > (10 ** 6):
        if n == 10 ** 12:
            return [1000000, 999999, 999999+1]
        c = n % limit
        a = limit
        b = (n - c) // a

        if c == 0:
            b -= 1
            c += limit

    return [a, b, c]


T = int(input())
for _ in range(T):
    n = int(input())
    print(*ans(n))
