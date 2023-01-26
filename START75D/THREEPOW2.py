def ans(s: str) -> int:

    # case 1, has exactly 3 1s in there.
    x = s.count("1")

    if x > 3:
        return False

    if x == 3:
        return True

    if x == 2:
        if len(s) < 2:
            return False
        return True

    # it's a power of two
    if x == 1:

        # if it's a power of two, but the total length is less than or equal to 2, then false
        if len(s) <= 2:
            return False
        return True

    return False


T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    if ans(s):
        print("YES")
    else:
        print("NO")
