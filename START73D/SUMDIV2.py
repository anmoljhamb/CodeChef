T = int(input())
for _ in range(T):
    x, y = list(map(int, input().split()))
    ans = x*y-x-y
    if (ans == -1):
        ans = max(x, y)-1
    if (ans == 0):
        ans = 2
    print(ans)
