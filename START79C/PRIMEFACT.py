import math


def ans(x: int, y: int) -> int:

    temp = {
        2: 5,
        3: 4,
        4: 4,
        5: 2,
        6: 3,
        8: 2,
        7: 1,
        9: 1,
        10: 1
    }

    if x == 7:
        y -= 14
    else:
        y -= 12

    return math.ceil(y / 2) + temp[x]


T = int(input())
for _ in range(T):
    x, y = list(map(int, input().split()))
    print(ans(x, y))
