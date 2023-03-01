T = int(input())
for _ in range(T):
    a, b = list(map(int, input().split()))
    a = 100 - a
    b = 100 - b

    a /= 100
    b /= 100

    if (a * 100 < b * 200):
        print("FIRST")
    elif (a * 100 > b * 200):
        print("SECOND")
    else:
        print("BOTH")
