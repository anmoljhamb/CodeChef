T = int(input())
for _ in range(T):
    x, y = list(map(int, input().split()))
    if y // 3 < x:
        print("NO")
    else:
        print("YES")
