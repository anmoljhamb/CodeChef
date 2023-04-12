def ans(arr: list, n: int) -> int:

    for i in range(1, n):
        arr[i] += arr[i-1]

    count = 0

    for i in range(n):
        if (arr[i] == (i+1)):
            count += 1

    return count


T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(ans(arr, n))
