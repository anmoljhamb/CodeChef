def ans(n: int):
    x = 2**(n-1)
    for i in range(x-n+1, x+1):
        temp = bin(i)[2:]
        print("0"*(n-len(temp))+temp)


T = int(input())
for _ in range(T):
    n = int(input())
    if (n == 2):
        print(-1)
    else:
        ans(n)
