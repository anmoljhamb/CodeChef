from functools import reduce


def isUnique(arr: list) -> bool:
    return len(set(arr)) == 1


T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, n):
        arr[i] = arr[i] ^ arr[i-1]
        arr[i-1] = 0

    if (arr[-1] == 0):
        print("YES")
    else:
        if (n & 1):
            print("YES")
        else:
            print("NO")
