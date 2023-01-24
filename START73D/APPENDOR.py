from functools import reduce


def sol(current: int, target: int) -> int:

    ans = 0
    count = 0
    while current > 0:

        current_bit = (current & 1) ^ (target & 1)

        if (current_bit == 1):
            if current & 1:
                return -1
            else:
                ans = ans | (1 << count)

        current = current >> 1
        target = target >> 1
        count += 1

    while target > 0:

        current_bit = target & 1

        if (current_bit == 1):
            ans = ans | (1 << count)

        count += 1
        target = target >> 1

    return ans


T = int(input())
for _ in range(T):
    N, target = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    temp = reduce(lambda x, y: x | y, arr)

    # print(temp, target)

    if (temp > target):
        print("-1")
    else:
        print(sol(temp, target))
