# def is_palin(s: str):
#     return s == s[::-1]


def ans(s: str, n: int):
    if n == 1:
        return -1

    # find all the possible indices for the letters, and if
    # all the letters occur only once, return -1.

    allOne = True
    freq = {}
    for index, char in enumerate(s):
        if char in freq:
            freq[char].append(index)
            allOne = False
        else:
            freq[char] = [index]

    if allOne:
        return -1

    return n-2


T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    print(ans(s, n))
