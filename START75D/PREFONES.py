def ans(s: str, n: int) -> int:

    x = s.count("1")
    if x == 0:
        return 0

    if x == n:
        return n

    max_count = 0
    i = 0
    temp_count = 0

    if (s[0] == "1"):
        temp_count += 1
        i = 1
        while i < n-1 and s[i] == "1":
            i += 1
            temp_count += 1

    while i < n:
        current_count = 0 + temp_count
        while i < n-1 and s[i+1] == "1":
            i += 1
            current_count += 1
        max_count = max(current_count, max_count)
        i += 1

    return max_count


T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    print(ans(s, n))
