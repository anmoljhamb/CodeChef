T = int(input())
for _ in range(T):
    x, y, z = list(map(int, input().split()))
    t = min(x, y, z)
    if (t == x):
        print("ALICE")
    elif t == y:
        print("BOB")
    else:
        print("CHARLIE")
