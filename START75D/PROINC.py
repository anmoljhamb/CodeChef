T = int(input())
for _ in range(T):
    x, y = list(map(int, input().split()))
    print(int(y+0.1*x))
