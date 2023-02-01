def ans(n: int, s: str):
    zeros = s.count('0')
    ones = n - zeros

    if (zeros == ones):
        return ones

    if (ones == 0):
        return 0

    if (zeros == 0):
        return 1

    if (zeros > ones):
        return ones

    if ones > zeros:
        return zeros + 1


T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    print(ans(n, s))
