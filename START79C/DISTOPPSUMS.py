T = int(input())
for _ in range(T):
    n = int(input())

    print(*list(range(1, n//2+1))[::-1], sep=" ", end=" ")
    print(*list(range(n//2+1, n+1)))
