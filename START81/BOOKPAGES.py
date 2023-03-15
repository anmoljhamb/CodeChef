def ans(arr: list, n: int) -> bool:
    return (sum(arr) % 2) == 0


T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if ans(arr, n) else "NO")
