def isUnique(*args):
    return len(set(args)) == len(args)


def ans(x, y, z):
    if x == y and y == z:
        if x == 1:
            return False
        return True
    if x == y or y == z or z == x:
        n = x + y + z
        for i in range(1, n):
            for j in range(1, n-i):
                k = n - i - j
                if isUnique(i, j, k) and k > 0:
                    return True
        return False
    return True


T = int(input())
for _ in range(T):
    x, y, z = list(map(int, input().split()))
    if ans(x, y, z):
        print("YES")
    else:
        print("NO")
