def ans(s: str, n: int, k: int) -> str:
    if s[0] == "1":
        return s + "0"*k

    return "1"+s[1:]+"0"*(k-1)


T = int(input())
for _ in range(T):
    n, k = list(map(int, input().split()))
    s = input()
    print(ans(s, n, k))
