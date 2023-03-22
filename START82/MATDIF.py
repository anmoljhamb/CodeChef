def ans(n: int) -> list[list]:

    count = 1
    arr = [[0 for _ in range(n)] for __ in range(n)]

    for i in range(n):
        for j in range(0, n, 2):
            arr[i][j] = count
            count += 1

    for i in range(n):
        for j in range(1, n, 2):
            arr[i][j] = count
            count += 1

    return arr


T = int(input())
for _ in range(T):
    n = int(input())
    for temp in ans(n):
        print(*temp, sep=" ")
