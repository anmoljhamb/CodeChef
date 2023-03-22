def ans(x: str, y: str, n: int) -> bool:
    if (x == y):
        return True

    if x[0] != y[0]:
        return False

    if x[-1] != y[-1]:
        return False

    x = list(x)
    y = list(y)

    if (len(set(x)) == 1):
        return False

    for i in range(n):
        if (x[i] != y[i]):
            if (x[i] == "1"):
                return False

    return True


T = int(input())
for _ in range(T):
    n = int(input())
    x = input().replace(" ", "")
    y = input().replace(" ", "")

    print("YES" if ans(x, y, n) else "NO")
