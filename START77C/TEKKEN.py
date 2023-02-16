def ans(a, b, c):
    temp = max(b, c) - min(b, c)
    if (a-temp) > 0:
        return True
    return False


T = int(input())
for _ in range(T):
    a, b, c = list(map(int, input().split()))
    print("YES" if ans(a, b, c) else "NO")
