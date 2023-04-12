def ans(n: int):

    if (n <= 2):
        return 0

    if (n % 2 == 0):
        ans = 2 + 1
        n -= 4
        n /= 2
        ans += 3 * n
        return ans

    ans = 2
    n -= 3
    n //= 2
    ans += 3 * n

    return ans


T = int(input())
for _ in range(T):
    n = int(input())
    print(int(ans(n)))
