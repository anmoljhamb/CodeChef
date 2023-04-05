T = int(input())
for _ in range(T):
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(len(list(filter(lambda y: y >= x, arr))))
