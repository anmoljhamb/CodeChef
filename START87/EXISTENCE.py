def ans(x: int, y: int):
    lhs = x ** 4 + 4 * (y*y)
    rhs = 4 * x * x * y
    return lhs == rhs


T = int(input())
for _ in range(T):
    x, y = list(map(int, input().split()))
    print("YES" if ans(x, y) else "NO")
