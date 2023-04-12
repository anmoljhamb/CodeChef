

def setBits(n: int):
    count = 0
    while n != 0:
        n = n & (n-1)
        count += 1
    return count


def ans(n: int) -> int:

    t = setBits(n)
    if (t < 3):
        return 0

    t -= 3
    temp = (t+2)*(t+1) // 2

    return (temp % (10 ** 9 + 7))


T = int(input())
for _ in range(T):
    n = int(input())
    print(ans(n))
