def ans(x: int, y: int) -> bool:
    if (x > 8):
        return False
    if x * y <= 500:
        return True
    return False


T = int(input())
for _ in range(T):
    x, y = list(map(int, input().split()))
    print("YES" if ans(x, y) else "NO")
