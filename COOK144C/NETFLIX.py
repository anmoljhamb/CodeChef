def ans(a, b, c, x):
    if (a+b) >= x:
        return True
    if (b+c) >= x:
        return True
    if (c+a) >= x:
        return True

    return False


T = int(input())
for _ in range(T):
    a, b, c, x = list(map(int, input().split()))
    print("YES" if ans(a, b, c, x) else "NO")
