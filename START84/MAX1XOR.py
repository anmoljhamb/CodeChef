def ans(s: list[int], n: int) -> int:

    list1 = [0]

    for i in range(1, n):
        list1.append(list1[i-1] ^ s[i-1])

    list2 = [1]

    for i in range(1, n):
        list2.append(list2[i-1] ^ s[i-1])

    return max(list1.count(1), list2.count(1))


T = int(input())
for _ in range(T):
    n = int(input())
    s = list(map(int, list(input())))
    print(ans(s, n))
