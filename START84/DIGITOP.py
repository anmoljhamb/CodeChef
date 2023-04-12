

def ans(arr1: list[int], arr2: list[int], n: int, k: int) -> bool:

    freqMap1 = {}
    for x in arr1:
        freqMap1[x] = (freqMap1[x]+1) if x in freqMap1 else 1

    freqMap2 = {}
    for x in arr2:
        freqMap2[x] = (freqMap2[x]+1) if x in freqMap2 else 1

    if (freqMap1 == freqMap2):
        return True

    print(freqMap1)
    print(freqMap2)

    return False


T = int(input())
for _ in range(T):
    n, k = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print("YES" if ans(arr1, arr2, n, k) else "NO")
