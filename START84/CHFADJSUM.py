

def ans(arr: list, n: int) -> bool:

    arr.sort()

    if n == 2:
        return False

    if (arr[0] == arr[-1]):
        # means that the entire array is the same.
        return False

    Z = arr[-1] + arr[-2]
    temp = []

    for i in range(n//2):
        temp.append(arr[n-i-1])
        temp.append(arr[i])

    if (n % 2 == 1):
        temp.append(arr[n//2])

    for i in range(n-1):
        if temp[i]+temp[i+1] >= Z:
            return False

    return True


T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if ans(arr, n) else "NO")
