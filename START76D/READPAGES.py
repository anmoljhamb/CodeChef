T = int(input())
for _ in range(T):
    n, x, y = list(map(int, input().split()))
    if (x * y >= n):
        print("YES")
    else:
        print("NO")
