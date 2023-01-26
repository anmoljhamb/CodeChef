T = int(input())
for _ in range(T):
    a, b, c, d = list(map(int, input().split()))
    set1 = set(range(a, b+1))
    set2 = set(range(c, d+1))

    print(len(set1)+len(set2)-len(set1.intersection(set2)))
