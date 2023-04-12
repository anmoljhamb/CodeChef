def ans(x: int, y: int) -> bool:
    return (x * 15) >= (2 * y)


T = int(input())
for _ in range(T):
    x, y = list(map(int, input().split()))
    print("YES" if ans(x, y) else "NO")
