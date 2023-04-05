from math import sqrt, floor, ceil


def ans(x: int, y: int):
    t = x - y
    return ceil((sqrt(1 + 8 * t) - 1) / 2)


T = int(input())
for _ in range(T):
    x, y = list(map(int, input().split()))
    print(ans(x, y))
