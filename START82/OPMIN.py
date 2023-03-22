def ans(arr: list, n: int):
    freq = {}
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return n-freq[min(arr)]


T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(ans(arr, n))
