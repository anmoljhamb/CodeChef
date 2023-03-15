def ans(n: int):
    for i in range(n, 2*n):
        temp = bin(i)[2:]
        print("0"*(n-len(temp))+temp)


T = int(input())
for _ in range(T):
    n = int(input())
    if (n == 2):
        print(-1)
    else:
        ans(n)
