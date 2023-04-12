from math import gcd


def util(arr: list, x: int) -> int:
    # returns index of the stuff to be popped.
    for index, k in enumerate(arr):
        if ((x % 2 == 0) and (k % 2 == 0)):
            return index
        if gcd(x, k) > 1:
            return index
    return 0


def ans(arr: list, n: int, queries: list, q: int):
    arr.sort()

    for x in queries:
        print(arr.pop(util(arr, x)), end=" ")


T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    queries = list(map(int, input().split()))

    ans(arr, n, queries, q)
