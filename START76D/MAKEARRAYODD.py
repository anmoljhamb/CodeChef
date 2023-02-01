def ans(arr: list, n: int, x: int):
    n_odd = 0
    for i in arr:
        if i & 1 == 1:
            n_odd += 1
    if (n_odd == n):
        return 0

    n_even = n-n_odd

    if (x & 1 == 0):
        if n_odd == 0:
            return -1
        else:
            return n_even
    else:
        if (n_even & 1 == 0):
            return n_even // 2
        else:
            return n_even // 2 + 1


T = int(input())
for _ in range(T):
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(ans(arr, n, x))
