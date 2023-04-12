def ans(arr: list[list[int]], n: int, m: int, k: int) -> int:

    highest_index = -1

    # loop through all the elements,
    # find the index with the higest value.
    # then, basically start filling all the elements from left to right
    # whatever? let's see.

    for i in range(n):
        for j in range(m):

    return n


T = int(input())
for _ in range(T):
    n, m, k = list(map(int, input().split()))
    arr = []
    temp = 0
    for __ in range(n):
        arr.append(list(map(int, input().split())))
        temp += sum(arr[-1])

    if (temp < (k-1)):
        print(-1)
    else:
        print(ans(arr, n, m, k))
